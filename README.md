# uamx-tos-acceptance
OpenEdx extension to enable users to accept terms and condition and keep track of their response

The project was created with [edx-cookiecutters](https://github.com/openedx/edx-cookiecutters/tree/master), a library for bootstraping OpenEdx extensions. This in particular is a **cookiecutter-django-app**.

## How to use it?

You should use this extension as an extra requirement for OpenEdx. In tutor, you can follow ["Installing extra requirements from private repositories"](https://docs.tutor.overhang.io/configuration.html#installing-extra-requirements-from-private-repositories) instructions.

To install this repo: 
```
# Download and setup as a private requirement
git clone git@github.com:UAMx/uamx-tos-acceptance.git "$(tutor config printroot)/env/build/openedx/requirements/uamx-tos-acceptance"
echo "-e ./uamx-tos-acceptance" >> "$(tutor config printroot)/env/build/openedx/requirements/private.txt"

# Rebuild the image to deploy changes
tutor images build openedx
tutor local launch -I
```

## Project structure



