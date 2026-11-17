"""Offer two Binder services in the launch (rocket) menu.

Adapted from the DraCor Textbook (dracor-org/dracor-textbook, docs/_ext).
sphinx-book-theme builds one Binder link from ``launch_buttons.binderhub_url``
(the EOSC EU Node Binder). This extension relabels that entry and adds a
second entry for the public mybinder.org, which needs no login, and a link
to the Textbook's instructions for launching notebooks.
"""

EU_NODE_BINDER = "https://binder.eu-2.notebooks.open-science-cloud.ec.europa.eu"
MYBINDER = "https://mybinder.org"
HELP_URL = (
    "https://dracor-org.github.io/dracor-textbook/"
    "appendix/running-the-textbook-as-an-interactive-notebook.html"
)


def add_mybinder_button(app, pagename, templatename, context, doctree):
    for group in context.get("header_buttons", []):
        if group.get("label") != "launch-buttons":
            continue
        buttons = group["buttons"]
        for i, button in enumerate(buttons):
            url = button.get("url", "")
            if not url.startswith(EU_NODE_BINDER):
                continue
            button.update(
                text="EOSC EU Node",
                tooltip=(
                    "Launch on the EOSC EU Node Binder (EU-2 cluster, "
                    "institutional login)"
                ),
                icon="fas fa-cloud",
            )
            buttons.insert(
                i + 1,
                {
                    "type": "link",
                    "text": "mybinder.org",
                    "tooltip": "Launch on mybinder.org (no login)",
                    "icon": "_static/images/logo_binder.svg",
                    "url": MYBINDER + url[len(EU_NODE_BINDER):],
                },
            )
            buttons.insert(
                i + 2,
                {
                    "type": "link",
                    "text": "How to launch (help)",
                    "tooltip": "DraCor Textbook, Appendix A: Running a notebook on Binder",
                    "icon": "fas fa-circle-question",
                    "url": HELP_URL,
                },
            )
            return


def setup(app):
    # Run after sphinx-book-theme has added the launch buttons (priority 501).
    app.connect("html-page-context", add_mybinder_button, priority=502)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
