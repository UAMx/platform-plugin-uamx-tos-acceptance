# UAMx Terms Of Service acceptance
OpenEdx extension to enable users terms of service acceptance, and keep track of their response

The project was created with [edx-cookiecutters](https://github.com/openedx/edx-cookiecutters/tree/master), a library for bootstraping OpenEdx extensions. This in particular is a **cookiecutter-django-app**.

## How to use it

This app integrates into the LMS and into the LMS admin: 
- in LMS, for an authenticated user, it shows an alert if the user have not accepted the terms and conditions yet and creates a page in the path `https://DOMAIN_NAME/uamx_tos_acceptance` showing the acceptance form.
- in LMS admin, at `https://DOMAIN_NAME/admin/uamx_tos_acceptance/termsofservice/`, shows a list of `TermsOfService` entries with one entry for each user, and the ability to switch the acceptance of the TOS. It also shows the date of creation / modification of the model.

![image](https://github.com/UAMx/uamx-tos-acceptance/assets/56433614/6ffc9e54-e70d-47a8-b9c1-5ab9ac767302)


## Installation and setup

You should use this extension as an extra requirement for OpenEdx. In tutor, you can follow ["Installing extra requirements from private repositories"](https://docs.tutor.overhang.io/configuration.html#installing-extra-requirements-from-private-repositories) instructions, which in summary is: 

```
# Download and setup uamx-tos-acceptance as a private requirement
git clone git@github.com:UAMx/uamx-tos-acceptance.git "$(tutor config printroot)/env/build/openedx/requirements/uamx-tos-acceptance"
echo "-e ./uamx-tos-acceptance" >> "$(tutor config printroot)/env/build/openedx/requirements/private.txt"

# Rebuild the image to deploy changes
tutor images build openedx
tutor local launch -I
```

## Project structure

This extension works just like any other Django app, where the app code is in `uamx-tos-acceptance/uamx_tos_acceptance`. The app is deployed to the docker image with `tutor images build openedx` and composed in `tutor local launch`. Is in the compose time where migrations are made and integrated into the db.

There are many other functionalities like unit tests and CI integration provided by the cookiecutter template which, at the moment, are not in use. 

> NOTE: currently we don't know how to notify mako of the templates used locally in this repo, so to inject them as part of the LMS (as in the screenshot below) you should add a template at `lms/templates/uamx_tos_acceptance` into the theme [like this](https://github.com/UAMx/uamx-theme/tree/main/lms/templates/uamx_tos_acceptance)
