"""Client to manage a local Docker-based instance of DraCor"""

import requests, json
from requests.auth import HTTPBasicAuth
from requests import ConnectionError
import logging
import uuid
import os
from xml.etree.ElementTree import ParseError
from xml.etree import ElementTree as ET
import base64
import subprocess
import yaml


def construct_request_url(
    api_base_url: str = "https://dracor.org/api/v1/",
    corpusname: str = None,
    playname: str = None,
    method: str = None):
    """Construct the request url

    Args:
        api_base_url (str, optional): Base URL of the DraCor API.
        corpusname (str, optional): Identifier of corpus 'corpusname'.
        playname (str, optional): Identifier of play 'playname'.
        method (str, optional): API method, e.g. "tei", "cast", ...
    """

    if api_base_url.endswith("/"):
        pass
    else:
        api_base_url = api_base_url + "/"

    if corpusname and playname:
        if method:
            request_url = f"{api_base_url}corpora/{corpusname}/plays/{playname}/{method}"
        else:
            request_url = f"{api_base_url}corpora/{corpusname}/plays/{playname}"
    elif corpusname and not playname:
        if method:
            request_url = f"{api_base_url}corpora/{corpusname}/{method}"
        else:
            request_url = f"{api_base_url}corpora/{corpusname}"
    elif method and not corpusname and not playname:
        request_url = f"{api_base_url}{method}"
    else:
        request_url = f"{api_base_url}info"

    return request_url


def api_get(
        api_base_url: str = "https://dracor.org/api/v1/",
        corpusname: str = None,
        playname: str = None,
        method: str = None,
        parse_json: bool = True):
    """Send GET request to a DraCor API

    Args:
        api_base_url (str, optional): Base URL of the DraCor API.
        corpusname (str, optional): Identifier of corpus 'corpusname'.
        playname (str, optional): Identifier of play 'playname'.
        method (str, optional): API method, e.g. "tei", "cast", ...
        parse_json (bool, optiona): Parse the result as JSON. Defaults to True.

    """
    request_url = construct_request_url(api_base_url=api_base_url,
                                        corpusname=corpusname,
                                        playname=playname,
                                        method=method)

    logging.debug(f"Will send GET request to: {request_url}")

    r = requests.get(request_url)

    assert r.status_code == 200, "Request was not successful. Server returned status code: " + str(r.status_code)

    if method == "tei":
        logging.debug("Requested TEI-XML, encoded in UTF-8.")
        return r.text.encode("utf-8")
    elif parse_json is True:
        json_data = json.loads(r.text)
        logging.debug("Parsed response to JSON.")
        return json_data
    else:
        logging.debug("Return data as is.")
        return r.text


def api_post(
        data,
        api_base_url: str = "https://dracor.org/api/v1/",
        corpusname: str = None,
        playname: str = None,
        method: str = None,
        username: str = "admin",
        password: str = "",
        headers: dict = None,
        payload_format: str = "json"):
    """Send POST request to a DraCor API

    Args:
        data: Data to include in the body of the POST request.
        api_base_url (str, optional): Base URL of the DraCor API.
        corpusname (str, optional): Identifier of corpus 'corpusname'.
        playname (str, optional): Identifier of play 'playname'.
        method (str, optional): API method, e.g. "tei", "cast", ...
        username (str, optional): Username of a user with write access. Defaults to "admin"
        password (str, optional): Password. Defaults to empty string ""
        headers (str, optional): Headers to include in the POST request
        payload_format (str, optional): Format of the payload. Defaults to "json".
    """
    request_url = construct_request_url(api_base_url=api_base_url,
                                        corpusname=corpusname,
                                        playname=playname,
                                        method=method)

    logging.debug(f"Will send POST request to: {request_url}")

    if username is not None and password is not None:
        logging.debug("Username and Password are set.")
        credentials = HTTPBasicAuth(username, password)
    else:
        logging.debug("Username and Password are NOT set.")
        credentials = None

    if data and headers and credentials:
        logging.debug("Send POST request with data, headers and credentials.")
        if payload_format == "json":
            r = requests.post(request_url, json=data, headers=headers, auth=credentials)
        else:
            r = requests.post(request_url, data=data, headers=headers, auth=credentials)
        logging.debug(f"Executed POST request. Server returned status code: {str(r.status_code)}")
        return r.status_code

    elif data and credentials and not headers:
        logging.debug("Send POST request with data and credentials, not headers.")
        if payload_format == "json":
            r = requests.post(request_url, json=data, auth=credentials)
        else:
            r = requests.post(request_url, data=data, auth=credentials)
        logging.debug(f"Executed POST request. Server returned status code: {str(r.status_code)}")
        return r.status_code

    elif data and headers and not credentials:
        logging.debug("Send POST request with data and headers, no credentials.")
        if payload_format == "json":
            r = requests.post(request_url, json=data, headers=headers)
        else:
            r = requests.post(request_url, data=data, headers=headers)
        logging.debug(f"Executed POST request. Server returned status code: {str(r.status_code)}")
        return r.status_code

    else:
        logging.debug("Send POST request without anything, only request url.")
        r = requests.post(request_url)
        return r.status_code


def api_put(data,
        api_base_url: str = "https://dracor.org/api/v1/",
        corpusname: str = None,
        playname: str = None,
        method: str = None,
        username: str = "admin",
        password: str = "",
        headers: dict = None):
    """Send PUT request to a DraCor API

        Args:
            data: Data to include in the body of the POST request.
            api_base_url (str, optional): Base URL of the DraCor API.
            corpusname (str, optional): Identifier of corpus 'corpusname'.
            playname (str, optional): Identifier of play 'playname'.
            method (str, optional): API method, e.g. "tei", "cast", ...
            username (str, optional): Username of a user with write access. Defaults to "admin"
            password (str, optional): Password. Defaults to empty string
            headers (dict, optional): HTTP headers to send with the request""
        """
    request_url = construct_request_url(api_base_url=api_base_url,
                                        corpusname=corpusname,
                                        playname=playname,
                                        method=method)

    logging.debug(f"Will send PUT request to: {request_url}")

    if username is not None and password is not None:
        logging.debug("Credentials are provided.")
        credentials = HTTPBasicAuth(username, password)
    else:
        logging.debug("Credentials are not provided.")
        credentials = None

    if data and headers and credentials:
        r = requests.put(request_url, data=data, headers=headers, auth=credentials)
        logging.debug(f"Executed PUT request. Server returned status code: {str(r.status_code)}")
        return r.status_code

    elif data and credentials and not headers:
        r = requests.put(request_url, data=data, auth=credentials)
        logging.debug(f"Executed PUT request. Server returned status code: {str(r.status_code)}")
        return r.status_code

    elif data and headers and not credentials:
        r = requests.put(request_url, data=data, headers=headers)
        logging.debug(f"Executed PUT request. Server returned status code: {str(r.status_code)}")
        return r.status_code

    else:
        r = requests.put(request_url)
        logging.debug(f"Executed PUT request. Server returned status code: {str(r.status_code)}")
        return r.status_code


def api_delete(
        api_base_url: str = "https://dracor.org/api/v1/",
        corpusname: str = None,
        playname: str = None,
        method: str = None,
        username: str = "admin",
        password: str = "",
        headers: dict = None):
    """Set DELETE request to a DraCor API

    Args:
        api_base_url (str, optional): Base URL of the DraCor API.
        corpusname (str, optional): Identifier of corpus 'corpusname'.
        playname (str, optional): Identifier of play 'playname'.
        method (str, optional): API method, e.g. "tei", "cast", ...
        username (str, optional): Username of a user with write access. Defaults to "admin"
        password (str, optional): Password. Defaults to empty string
        headers (dict, optional): HTTP headers to send with the request""
    """
    request_url = construct_request_url(api_base_url=api_base_url,
                                        corpusname=corpusname,
                                        playname=playname,
                                        method=method)

    logging.debug(f"Will send DELETE request to: {request_url}")

    if username is not None and password is not None:
        logging.debug("Credentials are provided.")
        credentials = HTTPBasicAuth(username, password)
    else:
        logging.debug("Credentials are not provided.")
        credentials = None

    if credentials and headers:
        r = requests.delete(request_url, headers=headers, auth=credentials)
        logging.debug(f"Executed DELETE request including headers and credentials. "
                      f"Server returned status code: {str(r.status_code)}")
        return r.status_code
    elif credentials and not headers:
        r = requests.delete(request_url, auth=credentials)
        logging.debug(f"Executed DELETE request including credentials, but no headers. "
                      f"Server returned status code: {str(r.status_code)}")
        return r.status_code
    else:
        r = requests.delete(request_url)
        logging.debug(f"Executed DELETE request (no headers, no credentials). "
                      f"Server returned status code: {str(r.status_code)}")
        return r.status_code


"""
Some ideas that have not been implemented yet:

- In parallel to corpora in the DB, the class should keep track of the status, e.g. information, if a play has been 
removed, added, ... so that it is always possible to retrieve a manifest file of a given corpus.
- store a corpus that has been compiled to a git repo, e.g. when adding plays from local, ... this is useful, when 
there are changes necessary that can't be included in DraCor but want to be persisted.
- change metadata of a corpus (there is no API function for this)
- lookup function DraCor - ID to corpusname+playname and vice versa
"""


class StableDraCor:
    """Stable Local DraCor instance
    """

    # URLs of external DraCor APIs
    __dracor_api_urls = dict(
        production="https://dracor.org/api/v1/",
        staging="https://staging.dracor.org/api/v1/",
    )

    def __init__(self,
                 api_base_url: str = None,
                 username: str = None,
                 password: str = None,
                 name: str = None,
                 description: str = None,
                 github_access_token: str = None):
        """

        Args:
             api_base_url (str, optional): URL of the local DraCor API. Default is set to http://localhost:8088/api/v1/
             username (str, optional): Username of the local instance. Default is set to "admin"
             password (str, optional): Password of the admin user of the local instance. Default is set to ""
             name (str, optional): Name of the local instance
             description (str, optional): Description of the local instance
             github_access_token (str, optional): Github Personal Access token used to indentify
                when sending API requests to the GitHub API. Allows for higher rate limit then anonymous requests.
        """

        # Set a uuid
        self.id = uuid.uuid4()
        logging.debug(f"Generated ID: {self.id}.")

        if name is not None:
            logging.debug(f"Set name to: {name}")
            self.name = name
        else:
            self.name = None

        if description is not None:
            logging.debug(f"Set description to: {name}")
            self.description = description
        else:
            self.description = None

        if api_base_url is not None:
            logging.debug(f"Update api_base_url with: {api_base_url}")
            self.api_base_url = api_base_url
        else:
            self.api_base_url = "http://localhost:8088/api/v1/"

        if username is not None:
            logging.debug(f"Update username with: {api_base_url}")
            self.__username = username
        else:
            logging.debug("Using default username 'admin'.")
            self.__username = "admin"

        if password is not None:
            logging.debug(f"Update password with: {api_base_url}")
            self.__password = password
        else:
            logging.debug("Using default password: ''.")
            self.__password = ""

        logging.info(f"Initialized new StableDraCor instance: '{self.name}' (ID: {self.id}).")

        if self.__test_api_connection() is True:
            logging.info(f"Local DraCor API is available at {self.api_base_url}.")
        else:
            logging.warning(f"Local DraCor API is not available at {self.api_base_url}.")

        if github_access_token is not None:
            self.__github_access_token = github_access_token
        else:
            self.__github_access_token = None
            logging.warning("Personal GitHub Access Token is not supplied. Requests to the GitHub API might be affected"
                            " by rate limiting.")

        # Check for the Operation System. Will output a Warning if working on Windows ;)
        self.__check_operation_system()

        # Check if Docker is installed. Will issue a warning if not
        self.__check_docker_installed()

        # Docker services
        # Initially assume, that there are no services running, but try to locate them in the next step
        self.services = dict(
            api=None,
            frontend=None,
            metrics=None,
            triplestore=None
        )

        # Try to detect running docker services
        self.__detect_docker_services()

        # List of images to push to dockerhub when calling the method
        self.__images_to_be_pushed = []

        # docker-compose file
        self.__docker_compose_file = None

    def __api_get(self, **kwargs):
        """Send GET request to running local instance. Uses the function api_get, but overrides api_base_url
        with the URL of the local instance"""
        return api_get(api_base_url=self.api_base_url, **kwargs)

    def __api_post(self, data, **kwargs):
        """Send POST request to running local instance. Uses the function api_post, but overrides api_base_url
        with the URL of the local instance

        Args:
            data: Payload to include in body

        """

        logging.debug(kwargs)
        return api_post(data, api_base_url=self.api_base_url, **kwargs)

    def __api_put(self, data, **kwargs):
        """Send PUT request to running local instance. Uses the function api_put, but overrides api_base_url
        with the URL of the local instance

        Args:
            data: Payload to include in body
        """
        logging.debug(kwargs)
        return api_put(data, api_base_url=self.api_base_url, **kwargs)

    def __api_delete(self, **kwargs):
        """Send DELETE request to running local instance. Uses the function api_delete, but overrides api_base_url
        with the URL of the local instance
        """
        logging.debug(kwargs)
        return api_delete(api_base_url=self.api_base_url, **kwargs)

    def __test_api_connection(self):
        """Test if local DraCor API is available."""
        try:
            self.__api_get()
            return True
        except ConnectionError:
            logging.debug("No API connection.")
            return False

    def __github_api_get(self,
                         api_call: str = None,
                         url: str = None,
                         headers: dict = None,
                         parse_json: bool = True,
                         **kwargs):
        """Send GET requests to the GitHub API.

        Args:
            api_call (str, optional): endpoint and parameters that should be sent to the GitHub API.
            url (str, optional): Full URL to GET data from GitHub API. If provided, api_call will be ignored.
            headers (dict, optional): Headers to send with the GET request. If provided on class instance level,
                will include the "Authorization" field with value of the personal access token and thus send authorized
                requests.
            parse_json (bool, optional): Parse the response as JSON. Defaults to True.

        """
        # Base-URL of the GitHub API
        github_api_base_url = "https://api.github.com/"

        if self.__github_access_token is not None:
            if headers is not None:
                headers["Authorization"] = f"Bearer {self.__github_access_token}"
            else:
                headers = dict(
                    Authorization=f"Bearer {self.__github_access_token}"
                )

        if api_call is not None and url is None:
            request_url = f"{github_api_base_url}{api_call}"
            logging.debug(f"Send GET request to GitHub: {request_url}")
        elif url is not None:
            request_url = url
            logging.debug(f"Provided full URL to send GET request to GitHub: {request_url}.")
        else:
            request_url = github_api_base_url
            logging.debug(f"No specialized API call (api_call) provided. Will send GET request to GitHub API "
                          f" base url.")

        if headers is not None:
            r = requests.get(url=request_url, headers=headers)
        else:
            r = requests.get(url=request_url)

        # logging.debug(r.headers)
        if "X-RateLimit-Remaining" in r.headers:
            if 1 < int(r.headers["X-RateLimit-Remaining"]) < 5:
                logging.warning(f"Approaching maximum API calls (rate limit). Remaining: "
                                f" {r.headers['X-RateLimit-Remaining']}")
            elif int(r.headers["X-RateLimit-Remaining"] == 1):
                logging.warning(f"Reached rate limit of {r.headers['X-RateLimit-Limit']}.")
                if self.__github_access_token is None:
                    logging.warning("Requests to GitHub API are probably unauthorized. Provide a personal "
                                    "access token to get a higher rate limit. "
                                    "See: https://docs.github.com/en/authentication/"
                                    "keeping-your-account-and-data-secure/managing-your-personal-access-tokens"
                                    "#creating-a-personal-access-token-classic")

        if r.status_code == 200:
            logging.debug(f"GET request to GitHub API was successful.")
            if parse_json is True:
                data = json.loads(r.text)
                return data
            else:
                return r.text
        # TODO implement the other status codes
        else:
            logging.debug(f"GET request was not successful. Server returned status code: {str(r.status_code)}.")
            logging.debug(r.text)

    def __check_docker_installed(self):
        """Helper Function to test if Docker is installed and can execute commands"""
        run_check = subprocess.run(["docker", "--version"], capture_output=True)
        docker_version_string = run_check.stdout.decode("utf-8")

        if "Docker version" in docker_version_string:
            logging.info(f"Docker is available.")
            return True
        else:
            logging.warning("Docker is not available and/or can not run subprocesses."
                            "Install Docker Desktop: https://www.docker.com/products/docker-desktop/")
            return False

    def __check_operation_system(self):
        """Helper Function to check if running on Windows."""
        operation_system = os.name
        logging.debug(f"Detected Operation System Type: '{operation_system}'")

        if operation_system == 'nt':
            logging.warning("The client has not been tested on Windows. There might be some limitations regarding "
                            " the management of Docker images/containers. Please report any bugs.")

        return operation_system

    def list_docker_images(self):
        """List Docker images available"""
        # docker images repo1 --format "{{json . }}"
        operation = subprocess.run(["docker", "images", "--format", '{{json . }}'], capture_output=True)
        items = operation.stdout.decode("utf-8").split("\n")
        images = []
        for item in items:
            if item != "":
                image = json.loads(item)
                images.append(image)
        return images

    def list_docker_containers(self,
                               only_running: bool = False) -> list:
        """

        Args:
            only_running (bool): Filter on running containers. Defaults to False

        Returns:
            list: Containers
        """
        if only_running is True:
            operation = subprocess.run(["docker", "ps", "--format", '{{json . }}'], capture_output=True)
        else:
            operation = subprocess.run(["docker", "ps", "-a", "--format", '{{json . }}'], capture_output=True)

        items = operation.stdout.decode("utf-8").split("\n")

        containers = []
        for item in items:
            if item != "":
                container = json.loads(item)
                containers.append(container)

        return containers

    def __detect_single_docker_service(self,
                                       name: str,
                                       expected_image: str,
                                       containers: list = None
                                       ):
        """Detect a single running Docker service based on the image used. We assume, that
        the containers are build with the standard images, e.g. dracor/dracor-api, ... and that we can filter
        for that.

        Args:
            name (str): Common name of the service, e.g. "api", "frontend", "tiplestore", "metrics"
            expected_image (str): Filter the containers by image. We look for the standard images, e.g.
                "dracor/dracor-api"
            containers (list, optional): A list of containers that will be filtered based on the expected_image
        """

        if containers is None:
            # if not set, get the running containers
            containers = self.list_docker_containers(only_running=True)

        container = list(filter(lambda item: f"{expected_image}" in item["Image"], containers))

        if len(container) == 0:
            logging.warning(f"Could not detect a running Docker container derived from a {expected_image} image.")
        elif len(container) == 1:
            container_id = container[0]["ID"]
            image = container[0]["Image"]
            logging.info(f"Found {expected_image} container with ID {container_id}. Image is: {image}")

            if self.services[name] is None:
                self.set_service(name=name, container=container_id, image=image)
            else:
                if "container" in self.services[name]:
                    if self.services[name]["container"] == container_id:
                        logging.debug(f"Container {name} already registered.")
                    else:
                        logging.warning(f"A different Docker container (ID: {self.services[name]['container']}) is"
                                        f" already registered as service {name}.")
                        logging.debug(f"Already registered container: {self.services[name]['container']}.")
                        logging.debug(f"Container that should be registed now: {container_id}.")

        else:
            logging.warning(f"Found {len(container)} running Docker containers derived from a '{expected_image}' "
                            f"image. Can not automatically detect if it is the database that shall be used. "
                            f"Set the container manually!")

    def __detect_docker_services(self):
        """Helper function to detect running services.

        can do this based on the image or the port?
         e.g. 'Ports': '0.0.0.0:8080->8080/tcp', (Port would probably be the better option for API/frontend)
        Ideally only one container would be running. This would be the container to work with."""

        running_containers = self.list_docker_containers(only_running=True)
        if len(running_containers) == 0:
            logging.debug("No running Docker containers found.")
        else:
            logging.debug(f"Detected {len(running_containers)} running Docker containers.")
            # logging.debug(running_containers)

        expected_service_images = dict(
            api="dracor/api",
            frontend="dracor/frontend",
            metrics="dracor/metrics",
            triplestore="dracor/fuseki"
        )

        for service_name in expected_service_images.keys():
            self.__detect_single_docker_service(name=service_name,
                                                expected_image=expected_service_images[service_name],
                                                containers=running_containers)

        # API/eXist could also be derived from dracor/stable-dracor:{tag} this should be also checked
        if self.services["api"] is None:
            self.__detect_single_docker_service(name="api",
                                                expected_image="dracor/stable-dracor",
                                                containers=running_containers)

    def __run_services_with_docker_compose(self,
                                           compose_file: str = None,
                                           url: str = None):
        """Run services with a docker compose file. Can use either a local compose file or use one that is
        downloaded from a URL.

        Args:
            compose_file (str, optional): Path to a compose file.
            url (str, optional): URL to a compose file.
        """
        if self.name:
            stack_name = self.name
        else:
            stack_name = "stable-dracor"

        if compose_file is None and url is None:
            logging.debug("No compose file provided. Will fetch from X, but this is not implemented yet.")
        # TODO: implement logic to get a compose file
        # first check if a path to a compose file is provided, if not
        # if not alert and fetch it from the source repo
        elif compose_file is not None:

            operation = subprocess.run(["docker",
                                        "compose",
                                        "-p",
                                        f"{stack_name}",
                                        "-f",
                                        compose_file,
                                        "up",
                                        "-d"])
            logging.debug(f"Started with docker compose file {compose_file}")
            self.__docker_compose_file = compose_file

            return True
        elif url is not None:
            logging.critical("Not implemented to start from a url. Need to supply compose file.")
            return False
        else:
            logging.warning("Can not start containers. Compose file not specified.")

        # TODO: list available images: https://docs.docker.com/docker-hub/api/latest/#tag/images/operation/GetNamespacesRepositoriesImages

    def run(self,
            compose_file: str = None):
        """Run a stack of DraCor Services
        TODO: this needs better documentation"""
        self.__run_services_with_docker_compose(compose_file=compose_file)

        # Try to detect running docker services
        self.__detect_docker_services()

    def __stop_docker_container_by_id(self, container_id:str):
        """Helper Function to stop a single Docker container identified by its ID"""
        stop_operation = subprocess.run(["docker", "stop", f"{container_id}"])

    def __stop_docker_stack(self):
        """Helper function to stop the whole docker stack
        docker compose -f {compose_file} stop does not work – maybe because of the containers
        running in detached mode, therefore we stop all containers in self.services..
        TODO: this should maybe return a status
        """
        for key in self.services.keys():
            container = self.services[key]["container"]
            self.__stop_docker_container_by_id(container)
            logging.info(f"Stopped container '{container}'.")

    def stop(self,
             container: str = None,
             service: str = None
             ):
        """Stop the whole stack (if no container ID supplied; or a single container)"""
        if container is not None and service is None:
            self.__stop_docker_container_by_id(container)
            logging.debug(f"Stopping container {container}.")
        elif service is not None and container is None:
            container = self.services[service]["container"]
            self.__stop_docker_container_by_id(container)
            logging.info(f"Stopping service '{service}' running as container {container}.")
        else:
            if self.__docker_compose_file is not None:
                logging.debug("Stopping all services.")
                self.__stop_docker_stack()
            else:
                logging.warning("Can not stop stack. No compose file is set.")

    def set_service(self,
                    name: str,
                    container: str,
                    image: str = None) -> dict:
        """Register a service (docker container) with the client

        Args:
            name (str): Name of the service (one of "api","frontend","metrics","triplestore")
            container (str): ID of the docker container running the service
            image (str, optional): Name/Tag of the image the container is based on

        Returns:
            dict: data on the service
        """
        if name not in ["api", "frontend", "metrics", "triplestore"]:
            logging.warning(f"Registering a non-canonical service: {name}")

        if self.services[name] is None:
            self.services[name] = dict(container=container)
        else:
            self.services[name]["container"] = container

        if image is not None:
            self.services[name]["image"] = image

        return self.services[name]

    def __create_docker_image_labels(self):
        """Helper Function to create Docker Labels to append when committing an image
        Creates a string that can be used in the docker commit command with the option -c or --change, e.g.
         LABEL multi.label1="value1" multi.label2="value2" other="value3"
        """

        label_data = {
            "org.dracor.stable-dracor.id": self.id
        }

        if self.name is not None:
            label_data["org.dracor.stable-dracor.name"] = self.name

        if self.description is not None:
            label_data["org.dracor.stable-dracor.description"] = self.description

        # org.dracor.stable-dracor.service-images:
        # contains the information about the images used for the DraCor microservices when creating the container
        service_images = {}
        for key in self.services.keys():
            service_images[key] = self.services[key]["image"]

        label_data["org.dracor.stable-dracor.service-images"] = json.dumps(service_images, separators=(',', ':'))

        labels = []

        for key in label_data.keys():
            label_string = f'{key}="{label_data[key]}"'
            labels.append(label_string)

        joined_labels = "LABEL " + " ".join(labels)

        return joined_labels

    def create_docker_image_of_service(self,
                                       service: str = "api",
                                       image_namespace: str = "dracor",
                                       image_name: str = "stable-dracor",
                                       image_tag: str = None,
                                       commit_message: str = None,
                                       update_services: bool = True):
        """Create a Docker image of one of the services, normally the dracor-api container.

        Args:
            service (str, optional): Name of the service to create an image of. Defaults to "api", but could be
                any of self.services.
            image_namespace (str, optional): Namespace the docker image will be added to. Defaults to "dracor".
            image_name (str, optional): Name of the image. Defaults to "stable-dracor"
            image_tag (str, optional): Tag of the image. This must be supplied if using dracor/stable-dracor.
                Defaults to id of the running system (not recommended to use).
            commit_message (str, optional): Commit message that will be used in the docker commit command.
            update_services (bool, optional): Replace the image in services with the newly created image.
                Defaults to True.
        """
        service_info = self.services[service]
        logging.debug(f"Creating image of service '{service}'.")

        container_id = service_info["container"]
        containers = self.list_docker_containers()

        container_data = list(filter(lambda item: item["ID"] == container_id, containers))[0]
        # logging.debug(container_data)
        container_state = container_data["State"]
        logging.debug(f"Container {container_id} is in state: {container_state}.")

        if container_state == "running" and service == "api":
            logging.warning("The dracor-api container is running. There might be issues with the image, if it is"
                            " create from a running container. Consider stopping it before creating the image.")

        """
        # make a clean shutdown of the eXist-DB container
        # on shutting down the database with xmlrpc see https://exist-db.org/exist/apps/doc/devguide_xmlrpc
        import xmlrpc.client
        s = xmlrpc.client.ServerProxy('http://localhost:8080/exist/xmlrpc')
        s.shutdown()
        """

        # TODO: Must test with Capek thing if it causes problems when committing a running container

        if image_tag is None:
            image_tag = self.id

        new_image = f"{image_namespace}/{image_name}:{image_tag}"

        if commit_message is None:
            commit_message = "Create image with StableDraCor client"

        labels = self.__create_docker_image_labels()

        commit_operation = subprocess.run([
            "docker",
            "commit",
            "-m",
            f'"{commit_message}"',
            "-c",
            f"{labels}",
            container_id,
            new_image],
            capture_output=True)

        new_image_sha = commit_operation.stdout.decode("utf-8")

        self.__images_to_be_pushed.append(new_image)

        logging.info(f"Committed container {container_id} as {new_image}. Image identifier {new_image_sha}.")

        if update_services is True:
            self.services[service]["image"] = new_image
            logging.debug(f"Updated services. Image {new_image} is set as service '{service}'.")

    def publish_docker_image(self,
                             user: str = None,
                             password: str = None,
                             logout: bool = True):
        """Push an image e.g. to Dockerhub
        Args:
            user (str, optional): Username on Dockerhub
            password (str, optional): Password on Dockerhub
            logout (bool, optional): Logout from docker after pushing the image
        """
        # docker login --username foo --password-stdin

        if user is not None and password is not None:
            password_bytes = bytes(password, "utf-8")
            login_operation = subprocess.run(
                ["docker", "login", "--username", f"{user}", "--password-stdin"], input=password_bytes, capture_output=True)
            logging.debug("Tried logging in to DockerHub: ")
            logging.debug(login_operation.stdout.decode("utf-8"))

        logging.debug(f"Following images will be pushed: {', '.join(self.__images_to_be_pushed)}.")

        for image in self.__images_to_be_pushed:
            push_operation = subprocess.run(["docker", "push", f"{image}"])

        logging.debug("Pushed images to DockerHub.")
        # reset
        self.__images_to_be_pushed = []

        if logout is True:
            logout_operation = subprocess.run(["docker", "logout"])
            logging.debug("Logged user out of Dockerhub.")

    def create_compose_file(self,
                            file_name: str = None):
        """Write the current configuration as a compose file

        Args:
            filename (str, optional): Overwrite the filename. Default will include self.name if available, else
                self.id.

        TODO: There is a lot of things hardcoded.. Better integrate self.services and the compose file
        """
        compose_file = dict(
            services={}
        )

        for key in self.services.keys():
            compose_file["services"][key] = {}
            compose_file["services"][key]["image"] = self.services[key]["image"]

            # This is currently hardcoded, maybe this should fetch these parts from the running system?

            if key == "api":

                compose_file["services"][key]["environment"] = [
                    "DRACOR_API_BASE=http://localhost:8088/api",
                    "EXIST_PASSWORD ="
                ]

                compose_file["services"][key]["ports"] = [
                    "8080:8080"
                ]

                compose_file["services"][key]["depends_on"] = [
                    "triplestore",
                    "metrics"
                ]

            elif key == "metrics":

                compose_file["services"][key]["ports"] = [
                    "8030:8030"
                ]

            elif key == "frontend":

                compose_file["services"][key]["environment"] = [
                    "DRACOR_API=http://api:8080/exist/restxq"
                ]

                compose_file["services"][key]["ports"] = [
                    "8088:80"
                ]

                compose_file["services"][key]["depends_on"] = [
                    "api"
                ]

            elif key == "triplestore":
                compose_file["services"][key]["environment"] = [
                    "ADMIN_PASSWORD=qwerty"
                ]

                compose_file["services"][key]["ports"] = [
                    "3030:3030"
                ]

        if self.name is not None:
            title = f"# Stable DraCor System '{self.name}'"
        else:
            title = "# Stable DraCor System"

        if file_name is None:
            if self.name is not None:
                file_name = f"compose.{self.name}.yml"
            else:
                file_name = f"compose.{self.id}.yml"

        with open(file_name, "w") as f:
            f.write(title)
            f.write("\n")
            yaml.dump(compose_file, f)
            logging.info(f"Stored configuration (docker-compose file) as {file_name}.")

    def load_info(self):
        """Should be able to load the info from the /info endpoint and store eXist-DB Version and API version.
        This information could be appended as docker labels when committing a running container.
        TODO: implement"""
        raise Exception("Not implemented.")

    def __corpus_exists(self, corpusname: str) -> bool:
        """Helper function to check if a corpus exists.
        The method checks if the provided identifier corpusname is in one of the fields "name" returned
        by the /corpora endpoint
        """
        logging.debug(f"Invoked __corpus_exists. Checking for corpora with name '{corpusname}'.")
        corpora = self.__api_get(method="corpora")
        result = list(filter(lambda corpus: corpusname in corpus["name"], corpora))
        if len(result) == 1:
            logging.debug(f"Corpus '{corpusname}' exists.")
            return True
        else:
            logging.debug(f"Corpus '{corpusname}' does not exist.")
            return False

    def add_corpus(self,
                   corpus_metadata: dict,
                   check: bool = True) -> bool:
        """Adds a corpus to the local instance.

        Documentation see https://dracor.org/doc/api#/admin/post-corpora

        Example of Corpus Metadata:
            {
                "name": "rus",
                "title": "Russian Drama Corpus",
                "repository": "https://github.com/dracor-org/rusdracor"
            }
        Args:
            corpus_metadata (dict): Metadata of corpus to add.
            check (bool, optional): Check if corpus exists after adding it. Defaults to True.

        Returns:
            bool: True if successful.
        """
        logging.debug(f"Adding corpus {corpus_metadata['name']}.")

        response = self.__api_post(
            corpus_metadata,
            method="corpora",
            username=self.__username,
            password=self.__password)

        if response == 200:
            logging.debug(f"Request to add corpus was successful.")

            if check is True:
                logging.debug("Running check for metadata of local corpus.")
                local_corpus_meta = self.__api_get(corpusname=corpus_metadata['name'])

                errors = []
                for field in corpus_metadata.keys():
                    if field in local_corpus_meta:
                        if local_corpus_meta[field] != corpus_metadata[field]:
                            errors.append(field)
                    else:
                        logging.debug(f"Field {field} not in metadata of created corpus.")
                        errors.append(field)
                logging.debug(f"Checked fields of metadata: {str(len(errors))} values did not match.")
                if len(errors) == 0:
                    logging.info(f"Successfully created corpus {local_corpus_meta['name']}. All metadata is available "
                                 f"and plays are available.")
                    return True
                elif len(errors) == 1 and errors[0] == "dramas":
                    logging.info(f"Successfully created corpus {local_corpus_meta['name']}. All metadata is available. "
                                 f"Plays have not been added yet.")
                    return True
                else:
                    logging.warning(f"Created corpus, but metadata {str(len(errors))} fields do not match: "
                                    f"Fields {','.join(errors)} are different.")
                    return True

            else:
                logging.debug("Did not check if local corpus exists.")
                logging.info(f"Successfully created corpus {corpus_metadata['name']}.")
                return True

        elif response == 409:
            logging.warning(f"Did not add corpus {corpus_metadata['name']}. Corpus already exists.")
            return False

    def copy_corpus_contents(self,
                             source_api_url: str = None,
                             source_corpusname: str = None,
                             target_corpusname: str = None,
                             exclude: list = None):
        """Copy the contents of a corpus identified by source_corpusname into the local DraCor instance.
        It is expected that the corpus exists in the local instance. Corpus metadata is not copied from the source.

        Args:
            source_api_url (str, optional): Url of the API to copy from. Default is https://dracor.org
            source_corpusname (str): Identifier "corpusname" in the source system
            target_corpusname (str, optional): Identifier "corpusname" in the local system.
                Default will take the name of the source corpus.
            exclude (list, optional): List of playnames to ignore. Per default all plays will be included.
        """

        if source_api_url is None:
            # use default production
            source_api_url = self.__dracor_api_urls["production"]

        logging.debug(f"Copying corpus contents of {source_corpusname} from {source_api_url}.")

        # If not explicitly set, use the corpus name of the source
        if target_corpusname is None:
            logging.debug(f"Target corpus name not set explicitly, will use source name: {source_corpusname}.")
            target_corpusname = source_corpusname

        source_plays = api_get(api_base_url=source_api_url, corpusname=source_corpusname)["plays"]
        logging.debug(f"Retrieved metadata of {str(len(source_plays))} plays from source.")

        errors = []

        # Plays to exclude
        if exclude is not None:
            exclude = exclude
        else:
            exclude = []

        for play in source_plays:
            if play["name"] in exclude:
                logging.debug(f"Play {play['name']} is excluded.")
            else:

                try:
                    logging.debug(f"Retrieving TEI of {play['name']}.")
                    tei = api_get(
                            api_base_url=source_api_url,
                            corpusname=source_corpusname,
                            playname=play["name"],
                            method="tei")

                    logging.debug(f"Storing TEI of {play['name']}.")

                    self.__api_put(
                            tei,
                            method="tei",
                            corpusname=target_corpusname,
                            playname=play["name"],
                            username=self.__username,
                            password=self.__password,
                            headers={"Content-Type": "application/xml"})

                except:
                    logging.warning(f"Could not add  {play['name']} to corpus f{target_corpusname}.")
                    errors.append(play["name"])

        logging.info(f"Added contents of corpus {source_corpusname} from {source_api_url}.")
        if exclude:
            logging.debug(f"Number of plays excluded: {len(exclude)}.")
        logging.debug(f"There were {len(errors)} Errors.")

    def copy_corpus(self,
                    source_api_url: str = None,
                    source_corpusname: str = None,
                    metadata: dict = None,
                    copy_contents: bool = True,
                    exclude: list = None,
                    check: bool = True):
        """Copy a corpus identified by source_corpusname into the local DraCor instance. This method creates the local
        corpus and copies the metadata from the source. Metadata can be overwritten by metadata. This will selectively
        overwrite the fields, data is provided for. If a corpus shall be renamed, pass {"name": "xyz"},...

        Args:
            source_api_url (str, optional): URL of the API to copy the data from. If not set will use DraCor production
            source_corpusname (str): Identifier "corpusname" of the corpus to copy from source
            metadata (dict, optional): Metadata fields to overwrite. Can be used to change the name of a corpus.
            copy_contents (bool, optional): Add the contents of the source corpus. Defaults to True.
            exclude (list, optional): List of identifiers of plays in the source corpus to ignore.
            check (bool, optional): Check if corpus is available after trying to copy. Defaults to True.
        """

        if source_api_url is None:
            # use default production
            source_api_url = self.__dracor_api_urls["production"]

        assert source_corpusname is not None, "Providing a corpusname from the source corpus is mandatory."

        logging.debug(f"Copying corpus {source_corpusname} from {source_api_url}.")

        # retrieve the metadata from the source corpus, default is https://dracor.org
        logging.debug("Retrieving corpus metadata.")
        original_corpus_metadata = api_get(api_base_url=source_api_url, corpusname=source_corpusname)

        new_corpus_metadata = original_corpus_metadata
        if metadata:
            logging.debug(f"Partially overwrite metadata:")
            for field in metadata.keys():
                new_corpus_metadata[field] = metadata[field]
                logging.debug(f"Overwritten metadata field {field} of new corpus.")

        # add the corpus, if returned True, everything went well
        corpus_add_status = self.add_corpus(corpus_metadata=new_corpus_metadata)

        if corpus_add_status is False:
            logging.warning(f"Copying corpus {source_corpusname} failed.")
            return False

        if copy_contents:
            self.copy_corpus_contents(
                source_api_url=source_api_url,
                source_corpusname=source_corpusname,
                target_corpusname=new_corpus_metadata["name"],
                exclude=exclude)

        if check is True:
            logging.debug(f"Checking if corpus {new_corpus_metadata['name']} is available.")
            try:
                local_corpus_data = self.__api_get(corpusname=new_corpus_metadata['name'])
                logging.debug(f"Retrieving corpus {new_corpus_metadata['name']} works.")
            except:
                return False
                logging.warning(f"Corpus {new_corpus_metadata['name']} is not available locally.")

            if copy_contents is True:
                logging.debug("Check if the number of plays are as expected:")
                original_play_count = len(original_corpus_metadata["plays"])
                local_play_count = len(local_corpus_data["plays"])
                if exclude is None:
                    expected_play_count = original_play_count
                else:
                    expected_play_count = original_play_count - len(exclude)
                logging.debug(f"Original play count: {str(original_play_count)}; "
                              f"Local play count: {str(local_play_count)}; "
                              f"Expected play count: {str(expected_play_count)}")

                if local_play_count == expected_play_count:
                    logging.info(f"Copying {original_corpus_metadata['name']} (as {new_corpus_metadata['name']}) was "
                                 f"successful. Plays (that were not excluded) were also copied entirely.")
                    return True
                else:
                    logging.warning("Corpus is available locally, but numbers of included plays are not as expected."
                                    "Not all requested plays could be copied. Check the logfile.")
                    return False
            else:
                logging.info(f"Copying {original_corpus_metadata['name']} metadata (as "
                             f"corpus {new_corpus_metadata['name']}) was successful. Plays were not copied.")
                return True

        else:
            logging.info(f"Copied corpus {source_corpusname} from {source_api_url}. Did not run a check.")
            return True

    def remove_corpus(self, corpusname: str = None):
        """Remove a corpus from the local instance"""

        assert corpusname, "Providing a corpusname is mandatory."

        logging.debug(f"Removing corpus {corpusname}")

        delete_status = self.__api_delete(corpusname=corpusname,
                                          username=self.__username,
                                          password=self.__password)
        if delete_status == 200:
            logging.info(f"Removed corpus {corpusname}.")
            return True
        if delete_status == 404:
            logging.warning(f"Could not remove corpus {corpusname}. No such corpus.")
            return False
        else:
            logging.debug(f"Server returned status code: {str(delete_status)}.")
            logging.info(f"Could not remove corpus {corpusname}.")
            False

    def remove_play_from_corpus(self,
                                corpusname: str = None,
                                playname: str = None):
        """Remove a play from a corpus

        Args:
            corpusname (str): Identifier "corpusname" the play is contained in.
            playname (str): Identifier "playname" of a play.
            TODO: could add check to see if play is removed?
        """
        assert corpusname is not None, "Providing a corpusname is mandatory."
        assert playname is not None, "Providing a playname is mandatory."

        remove_status = self.__api_delete(corpusname=corpusname, playname=playname)
        if remove_status == 200:
            logging.info(f"Removed play {playname} from corpus {corpusname}.")
            return True
        if remove_status == 404:
            logging.warning(f"No such play {playname} in {corpusname}.")
            return False
        else:
            logging.debug(f"Unknown error code returned by delete operation: {str(remove_status)}")
            return False

    def add_plays_from_directory(self,
                                 corpusname: str,
                                 directory: str,
                                 corpus_metadata: dict = None
                                 ):
        """Load local data and add it to a corpus identified by corpusnam.
        If the corpus does not exist, it will be created with minimal metadata.

        Args:
            corpusname (str): Identifier 'corpusname' of the corpus to add the plays to
            directory (str): Path to the local directory
            corpus_metadata (dict, optional): Metadata of the corpus to create
            """

        assert os.path.exists(directory), f"The directory {directory} does not exist."

        files = os.listdir(directory)
        logging.debug(files)

        logging.debug(f"Checking if corpus '{corpusname}' already exists.")
        corpus_exist = self.__corpus_exists(corpusname)

        if corpus_exist is False:
            logging.debug(f"Corpus '{corpusname}' does not exist. Need to create it.")

            if corpus_metadata:
                logging.debug("Corpus metadata is provided. Try to create the corpus with this metadata.")
                # if the method add_corpus returns True, the corpus has been created
                create_corpus_status = self.add_corpus(corpus_metadata)

                assert create_corpus_status is True, f"Could not create '{corpusname}' with provided metadata. " \
                                                     f"Plays can not be be loaded."

            else:
                logging.debug(f"No metadata provided for corpus."
                              f" Will create a corpus with the name '{corpusname}'")
                new_corpus_metadata = {"name": corpusname, "title": "No title provided."}
                self.add_corpus(corpus_metadata=new_corpus_metadata)

                assert self.__corpus_exists(corpusname) is True, f"Failed to create corpus {corpusname}."
        success = []
        errors = []

        for file in files:
            logging.debug(f"Importing {file} from directory {directory}.")
            import_flag = True

            filepath = directory + "/" + file
            if ".xml" in file:
                playname = file.split(".xml")[0]
            else:
                logging.debug("Maybe not an xml file according to the file extension.")
                import_flag = False

            # parsing the xml would not be necessary for import but this checks if the file is wellformed
            # otherwise the API would reject it but I am not sure, what the API would return as error code
            if import_flag is True:
                try:
                    xml = ET.parse(filepath)
                except ParseError:
                    logging.warning(f"File at '{filepath}' is not well-formed XML. Can not add '{file}'."
                                    f"Should also check if file extension is '.xml'!")
                    import_flag = False

            if import_flag is True:

                with open(filepath, "r") as f:
                    tei = f.read().encode("utf-8")
                    self.__api_put(
                        tei,
                        method="tei",
                        corpusname=corpusname,
                        playname=playname,
                        username=self.__username,
                        password=self.__password,
                        headers={"Content-Type": "application/xml"})

                success.append(file)
                logging.info(f"Added TEI data from file '{file}' to corpus '{corpusname}'.")

        if len(errors) == 0:
            logging.info(f"Imported {str(len(success))} files from {directory} as corpus '{corpusname}'.")
            return True
        else:
            logging.debug(f"Number of successful imports: {str(len(success))}.")
            logging.debug(f"Number of errors: {str(len(errors))}.")
            logging.debug(errors)
            return False

    def add_play_version_to_corpus(self,
                                   corpusname: str = None,
                                   playname: str = None,
                                   commit: str = None,
                                   filename: str = None,
                                   repository_name: str = None,
                                   repository_owner: str = "dracor-org",
                                   repository_data_folder: str = "tei",
                                   repository_blob_base_url: str = "raw.githubusercontent.com",
                                   protocol: str = "https",
                                   check: bool = True) -> bool:
        f"""Add a play in a certain version from a git repository defined by a git commit to a corpus.

        Args:
            corpusname (str, optional): Identifier 'corpusname' of the local target corpus. 
                If not set the mandatory repository_name will be used.
            playname (str, optional): Identifier 'playname' in the target corpus. This is the name, the play will get.
                If not set the mandatory filename will be used.
            commit (str, optional): Commit-ID identifying a Version of the data in the repository.
                If not set it will use the most recent data from the "main" branch.
            filename (str): File name of the file containing the play data. The file extension ".xml" will be added.
            repository_name (str): Name of the repository. This must not match the corpusname, e.g. "gerdracor".
            repository_owner (str): Username of the user owning the repository. Defaults to "dracor-org"
            repository_data_folder (str, optional): Path from the root folder of the repository to the folder containing 
                the files. Defaults to "tei"
            repository_blob_base_url (str): Base url to retrieve a blob/raw data from the repository. 
                Defaults to "raw.githubusercontent.com"
            protocol (str, optional): Protocol used in the request url. Defaults to "https"
            check (bool, optional): Additional check if the play has been successfully added. Defaults to True.
        """

        assert repository_name is not None, "Providing the name of a repository (repository_name) is required."
        assert filename is not None, "Providing a file name (filename) is required."

        if commit is None:
            logging.debug(f"Commit not set, will try to use latest version of {filename} from main branch.")
            commit = "main"

        if filename.endswith(".xml"):
            checked_filename = filename
        else:
            checked_filename = f"{filename}.xml"

        source_url = f"{protocol}://{repository_blob_base_url}/{repository_owner}/{repository_name}/{commit}/" \
                     f"{repository_data_folder}/{checked_filename}"

        logging.debug(f"Fetching github data from source url: {source_url}")

        r = requests.get(url=source_url)
        if r.status_code == 200:
            import_flag = True
            tei = r.text.encode("utf-8")
            logging.debug(f"Could retrieve data from '{source_url}'.")
        else:
            import_flag = False
            logging.debug(f"Retrieving data from '{source_url}' failed. Server returned: {str(r.status_code)}.")

        # try to parse xml
        if import_flag is True:
            try:
                xml = ET.fromstring(tei)
                logging.debug("Could parse returned data. XML is well-formed.")
            except ParseError:
                logging.warning(f"File at url '{source_url}' is not well-formed XML. Can not add it to the database.")
                import_flag = False

        if corpusname is None:
            logging.debug(f"Name of the target corpus is not provided. "
                          f" Using the name of the repository '{repository_name}' as name of the corpus.")
            corpusname = repository_name

        if self.__corpus_exists(corpusname) is False:
            logging.debug(f"Must create corpus '{corpusname}'.")
            new_corpus_metadata = {"name": corpusname,
                                   "title": "Automatically generated corpus",
                                   "description": "This corpus has been created automatically "
                                                  "because it did not exist during an import operation."}
            self.add_corpus(corpus_metadata=new_corpus_metadata, check=False)

        if playname is None:
            playname = filename.replace(".xml", "")
            logging.debug(f"Identifier 'playname' of the play is not set. Will use filename '{filename}' as "
                          f" the identifier of the play: ('{playname}').")

        if import_flag is True:
            add_status = self.__api_put(
                tei,
                method="tei",
                corpusname=corpusname,
                playname=playname,
                username=self.__username,
                password=self.__password,
                headers={"Content-Type": "application/xml"})

            if add_status == 200:
                logging.debug("PUT request to add data was successful.")
            elif add_status == 404:
                logging.debug(f"PUT request not successful. Corpus {corpusname} probably "
                              f" does not exist. Can not add the data.")
                import_flag = False
            else:
                logging.debug(f"PUT request to add data was not successful. Status code. {add_status}.")
                import_flag = False

        if check is True and import_flag is True:
            logging.debug(f"Checking if play '{playname}' has been added to corpus '{corpusname}'.")
            added_play = self.__api_get(corpusname=corpusname, playname=playname)
            if type(added_play) == dict:
                logging.info(f"Play '{playname}' retrieved from '{source_url}' has been successfully added "
                             f"to corpus '{corpusname}'. Checked and found local play data.")
                return True
            else:
                logging.warning(f"Play from '{source_url}' has not been added.")
                return False
        elif import_flag is True and check is False:
            logging.info(f"Data of play '{playname}' retrieved from '{source_url}' most likely has been"
                         f" added to corpus '{corpusname}'. Did not run additional check.")
            return True
        elif import_flag is False:
            logging.warning(f"Could not add play from source '{source_url}'.")
            return False
        else:
            logging.debug("This else statement should not be reachable.")
            return False

    def __get_latest_commit_hash_in_github_repo(self,
                                                repository_name: str,
                                                repository_owner: str = "dracor-org") -> str:
        """Use the GitHUb API to get the commit-ID of the latest commit on a repository.
        The method will get Github commits by using /repos/{owner}/{name}/commits. We assume that the first entry in
        this list is the latest commit, but we have to tested it yet.

        For example, a commit hash is necessary to retrieve the tree and thus the files at a given point in time.

        Args:
            repository_owner (str, optional): User owning the repository. Defaults to "dracor-org"
            repository_name (str): Name of the repository.

        TODO: Investigate if the first returned commit is the latest commit indeed.
        """
        get_commits_api_call = f"repos/{repository_owner}/{repository_name}/commits"
        data = self.__github_api_get(api_call=get_commits_api_call)

        if data is not None:
            commit_data = data[0]
            commit_hash = commit_data["sha"]
            logging.debug(f"Retrieved latest (?) commit of repo '{repository_owner}/{repository_name}': {commit_hash}.")
            return commit_hash

    def list_plays_in_repo(self,
                                  commit: str = None,
                                  repository_name: str = None,
                                  repository_owner: str = "dracor-org",
                                  repository_base_url: str = "github.com",
                                  repository_data_folder: str = "tei"
                                  ):
        """List TEI-XML files of plays in a repository. This has been tested with GitHub only.

        Args:
            commit (str, optional): Commit-ID representing the state of the repository at a given point in time.
                If it is not set, the (probably) latest commit will be used.
            repository_name (str): Name of the repository
            repository_owner: Username of the user owning the repository. Defaults to "dracor-org"
            repository_base_url: Base of the repository. If it is the default "github.com", the Github API will be used.
            repository_data_folder: Path from root to folder containing the play data. Defaults to "tei"

        Returns:
            list: List containing the file names of plays included in the repo at a point in time identified by a commit
        """
        assert repository_name is not None, "Providing a repository name is mandatory!"

        if commit is None:
            logging.debug("No commit set. Getting latest commit.")
            commit = self.__get_latest_commit_hash_in_github_repo(repository_name=repository_name,
                                                                  repository_owner=repository_owner)
        if repository_base_url != "github.com":
            logging.critical(f"Not using Github. This is only implemented for the Github API. Will probably fail.")

        logging.debug(f"Using Github to get the commit {commit} and the tree object thereof.")
        get_commit_api_call = f"repos/{repository_owner}/{repository_name}/commits/{commit}"
        commit_data = self.__github_api_get(api_call=get_commit_api_call)
        tree = commit_data["commit"]["tree"]
        logging.debug(f"Got the Github tree of commit '{commit}': {tree['sha']} at url {tree['url']}.")

        if "/" in repository_data_folder:
            logging.critical(f"Getting data in nested directories is not implemented. Can only get the contents of"
                             f" a single data folder contained in the repository root.")

        # get the tree and then the hash of the tree of the sub-folder
        repository_root_folder = self.__github_api_get(url=tree["url"])

        # this is not the very best check in the world
        if type(repository_root_folder) == dict:
            if repository_root_folder["truncated"] is True:
                logging.warning("Not all items in the root folder of the repository are included in the response.")

            tree_objects_in_root_folder = repository_root_folder["tree"]
            data_folder_object = list(filter(lambda item: item["path"] == repository_data_folder,
                                             tree_objects_in_root_folder))[0]
            logging.debug(data_folder_object)
            logging.debug(f"Found data folder '{repository_data_folder}' in tree objects. "
                          f" sha: {data_folder_object['sha']}, url: {data_folder_object['url']}.")

        else:
            logging.warning(f"GET request to get the data '{repository_data_folder}' folder failed!")
            data_folder_object = None

        if data_folder_object is not None:
            logging.debug(f"Getting files in the data folder.")
            parsed_data_folder_tree_object = self.__github_api_get(url=data_folder_object["url"])

            # This is not the very best check in the world
            if type(parsed_data_folder_tree_object) == dict:

                if parsed_data_folder_tree_object["truncated"] is True:
                    logging.warning("The contents of the TEI folder are paged! Need to implement!")

                file_objects = parsed_data_folder_tree_object["tree"]
                logging.debug(f"Found {len(file_objects)} in the data folder tree.")

                filenames = []

                for item in file_objects:
                    # exclude directories
                    if item["type"] == "blob":
                        filenames.append(item["path"])

            else:
                logging.warning(f"GET request to retrieve the contents of the data folder failed.")
                filenames = []

            return filenames

    def add_corpus_from_repo(self,
                             commit: str = None,
                             repository_name: str = None,
                             repository_owner: str = "dracor-org",
                             repository_base_url: str = "github.com",
                             repository_data_folder: str = "tei",
                             use_metadata_of_corpus_xml: bool = True,
                             corpus_metadata: dict = None,
                             exclude: list = None) -> bool:
        """Add a corpus from a repository

        Args:
            commit (str, optional): Commit-ID representing the state of the repository at a given point in time.
                If it is not set, the (probably) latest commit will be used.
            repository_name (str): Name of the repository
            repository_owner: Username of the user owning the repository. Defaults to "dracor-org"
            repository_base_url: Base of the repository. If it is the default "github.com", the Github API will be used.
            repository_data_folder (str, optional): Path to the folder containing the files. Defaults to "tei"
            use_metadata_of_corpus_xml (bool, optional): Use the file "corpus.xml" in the root folder for metadata.
            corpus_metadata (dict, optional): Metadata to overwrite corpus metadata with.
            exclude (list, optional): File names (without file extension .xml) of plays to exclude from new corpus.

        Returns:
            bool: True if successful
        TODO: There seems to be some issues when trying to add CzeDracor
        """
        assert repository_name is not None, "Providing a repository name is required!"

        if commit is None:
            logging.debug("No commit set. Getting latest commit.")
            commit = self.__get_latest_commit_hash_in_github_repo(repository_name=repository_name,
                                                                  repository_owner=repository_owner)

        if use_metadata_of_corpus_xml is True:
            logging.debug(f"Get the repository root folder tree at commit '{commit}'.")

            get_commit_api_call = f"repos/{repository_owner}/{repository_name}/commits/{commit}"
            commit_data = self.__github_api_get(api_call=get_commit_api_call)

            if type(commit_data) == dict:
                tree = commit_data["commit"]["tree"]
                logging.debug(f"Got the Github tree of commit '{commit}': {tree['sha']} at url {tree['url']}.")
            else:
                logging.debug(f"Getting the tree from GitHub was not successful.")
                tree = None

            if tree is not None:
                root_folder_tree_data = self.__github_api_get(url=tree["url"])

                if type(root_folder_tree_data) == dict:
                    items = root_folder_tree_data["tree"]
                    corpus_xml_object = list(filter(lambda item: item["path"] == "corpus.xml",
                                             items))[0]
                    # logging.debug(corpus_xml_object)

                    if corpus_xml_object["type"] == "blob":
                        corpus_xml_blob_url = corpus_xml_object["url"]
                        logging.debug(f"Found corpus.xml blob at {corpus_xml_blob_url}.")
                    else:
                        logging.debug(f"Could not find url of corpus.xml blob.")
                        corpus_xml_blob_url = None
                else:
                    logging.debug(f"Requesting the tree of the root folder was not successful.")
                    corpus_xml_blob_url = None

            if corpus_xml_blob_url is not None:
                # TODO: Continue here. Need to change to get_github_api stuff
                blob_data = self.__github_api_get(url=corpus_xml_blob_url)
                if "content" in blob_data:
                    corpus_xml_string = base64.b64decode(blob_data["content"])
                    corpus_xml = ET.fromstring(corpus_xml_string)
                else:
                    logging.warning(f"Could not decode and parse corpus.xml. Operation might fail.")
                    corpus_xml = None

            if corpus_xml is not None:
                ns = {"tei": "http://www.tei-c.org/ns/1.0"}
                logging.debug("Extracting corpus metadata from corpus.xml.")

                existing_corpus_metadata = {}

                corpus_title_e = corpus_xml.find("tei:teiHeader/tei:fileDesc/tei:titleStmt/tei:title", ns)
                if corpus_title_e is not None:
                    corpus_title = corpus_title_e.text
                    existing_corpus_metadata["title"] = corpus_title
                    logging.debug(f"Title: {corpus_title}")

                corpus_name_e = corpus_xml.find("tei:teiHeader/tei:fileDesc/tei:publicationStmt/tei:idno[@type='URI']",
                                                ns)
                if corpus_name_e is not None:
                    corpus_name = corpus_name_e.text
                    existing_corpus_metadata["name"] = corpus_name
                    logging.debug(f"Corpusname: {corpus_name}")

                corpus_desc_elems = corpus_xml.findall("tei:teiHeader/tei:encodingDesc/tei:projectDesc/tei:p", ns)
                if len(corpus_desc_elems) != 0:
                    corpus_desc_texts = []
                    for elem in corpus_desc_elems:
                        corpus_desc_texts.append(elem.text)
                    corpus_desc_text = "".join(corpus_desc_texts)
                    existing_corpus_metadata["description"] = corpus_desc_text
                    logging.debug(f"Description: {corpus_desc_text}")
                    # TODO: this ignores included sub-elements, e.g. links

                # TODO: Extract other metadata, e.g. licence, licenceUrl, and whatnot

        if corpus_metadata is not None:
            logging.debug("Prepare corpus metadata for creating corpus.")

            if existing_corpus_metadata:
                logging.debug("Overwriting corpus.xml extracted data with the provided corpus metadata.")
                new_corpusmetadata = existing_corpus_metadata
            else:
                new_corpusmetadata = {}

            for key in corpus_metadata.keys():
                new_corpusmetadata[key] = corpus_metadata[key]

        elif existing_corpus_metadata is not None:
            new_corpusmetadata = existing_corpus_metadata

        else:
            logging.debug("Did not provide corpus metadata and not using corpus.xml.")
            new_corpusmetadata = {"name": repository_name,
                                  "title": "No title provided",
                                  "description": "Corpus was created automatically during import of corpus "
                                                 " repository from GitHub. The repository did not contain a"
                                                 " corpus.xml file with corpus metadata."}

        if "name" not in new_corpusmetadata:
            logging.debug(f"No identifier corpusname for target corpus supplied. Use name of source repository"
                          f" '{repository_name}'.")
            new_corpusmetadata["name"] = repository_name

        create_corpus_status = self.add_corpus(corpus_metadata=new_corpusmetadata, check=False)

        filenames = self.list_plays_in_repo(commit=commit,
                                            repository_owner=repository_owner,
                                            repository_name=repository_name,
                                            repository_base_url=repository_base_url,
                                            repository_data_folder=repository_data_folder)
        logging.debug(f"Got {len(filenames)} filenames from repo {repository_owner}/{repository_name}.")

        success = []
        errors = []

        if exclude is None:
            logging.debug("No plays are to be excluded.")
            exclude = []

        for filename in filenames:
            if filename in exclude or f"{filename}.xml" in exclude:
                logging.debug(f"File {filename} is excluded.")
                pass
            else:
                add_file_status = self.add_play_version_to_corpus(
                    corpusname=new_corpusmetadata["name"],
                    commit=commit,
                    filename=filename,
                    repository_name=repository_name,
                    repository_owner=repository_owner)
                if add_file_status is True:
                    success.append(filename)
                else:
                    errors.append(filename)

        if len(errors) == 0:
            logging.info(f"Successfully added all {len(success)} files to {new_corpusmetadata['name']}.")
            return True
        else:
            logging.warning(f"Added {len(success)} of {len(filenames)} to corpus {new_corpusmetadata['name']}."
                            f"{len(errors)} errors occurred. Files, that were not added: {', '.join(errors)}.")
            return False

    def list_dracor_github_repos(self):
        """List available Repositories of dracor-og on Github. This should allow for excluding
        repositories that don't have a corpus.xml file in the root directory and no folder "tei" containing xml files
        """
        raise Exception("Not implemented.")


