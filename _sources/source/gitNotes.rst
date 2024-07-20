Git Notes
=========

This project uses a Gitflow Workflow tailored for a single developer,
focusing on maintaining a main branch with feature, release, and hotfix
branches.

Gitflow Workflow Overview
-------------------------

The Gitflow Workflow is ideal for managing complex projects with
multiple release stages. Here’s a detailed explanation of how to use
this workflow in your project:

1.  **Create a Feature Branch**: For each new feature, create a new
    branch off the ``development`` branch. Use descriptive names like
    ``feature/add-login``.

    .. code:: bash

       git checkout -b feature/your-feature-name development

2.  **Make Commits**: Commit your changes in small, logical chunks with
    clear and descriptive commit messages.

    .. code:: bash

       git add .
       git commit -m "Add user login feature"

3.  **Push Feature Branch to Remote**: Regularly push your branch to the
    remote repository to back up your work.

    .. code:: bash

       git push origin feature/your-feature-name

4.  **Finish Feature Branch**: Once your feature is complete, merge it
    back into the ``development`` branch.

    .. code:: bash

       git checkout development
       git pull origin development
       git merge feature/your-feature-name
       git push origin development

5.  **Clean Up**: After merging, delete the feature branch locally and
    remotely to keep your branch list clean.

    .. code:: bash

       git branch -d feature/your-feature-name
       git push origin --delete feature/your-feature-name

6.  **Create a Release Branch**: When you’re ready to prepare a new
    release, create a release branch from ``development``.

    .. code:: bash

       git checkout -b release/1.0.0 development

7.  **Finalize the Release**: Finalize your release by merging the
    release branch into both ``main`` and ``development``, then tag the
    release.

    .. code:: bash

       git checkout main
       git merge release/1.0.0
       git tag -a v1.0.0 -m "Release v1.0.0"
       git push origin main --tags

       git checkout development
       git merge release/1.0.0
       git push origin development

8.  **Clean Up Release Branch**: After merging, delete the release
    branch locally and remotely.

    .. code:: bash

       git branch -d release/1.0.0
       git push origin --delete release/1.0.0

9.  **Create a Hotfix Branch**: For urgent fixes on production, create a
    hotfix branch from ``main``.

    .. code:: bash

       git checkout -b hotfix/1.0.1 main

10. **Apply the Hotfix**: Commit your hotfix and merge it back into both
    ``main`` and ``development``.

    .. code:: bash

       git add .
       git commit -m "Fix critical issue"
       git checkout main
       git merge hotfix/1.0.1
       git tag -a v1.0.1 -m "Hotfix v1.0.1"
       git push origin main --tags

       git checkout development
       git merge hotfix/1.0.1
       git push origin development

11. **Clean Up Hotfix Branch**: After merging, delete the hotfix branch
    locally and remotely.

    .. code:: bash

       git branch -d hotfix/1.0.1
       git push origin --delete hotfix/1.0.1

Commit Message Template
-----------------------

A good commit message should explain what and why rather than how. Use
the following template to structure your commit messages:

.. code:: markdown

   Type: Short description of the change (use imperative mood)

   Detailed explanation of the change and its context, if necessary. Include references to issues or tickets (e.g., "Closes #123").

Commit Message Examples
~~~~~~~~~~~~~~~~~~~~~~~

Examples
^^^^^^^^

-  **Feature Addition**:

   .. code:: markdown

      feat: add user login feature

      Add a new feature that allows users to log in using their email and password. This includes the login form, validation, and API integration. Closes #45.

-  **Bug Fix**:

   .. code:: markdown

      fix: resolve issue with user session timeout

      Fix a bug that caused user sessions to timeout prematurely. The session duration is now correctly set to 30 minutes. Closes #67.

Commit Types
^^^^^^^^^^^^

-  **feat**: New feature
-  **fix**: Bug fix
-  **refactor**: Rewrite/restructure code
-  **perf**: Performance improvements
-  **style**: Non-functional update (white space, formatting, missing
   semi-colons, …)
-  **test**: Test management/correcting
-  **docs**: Documentation updates
-  **build**: Build components updates (build tool, dependencies,
   project version, …)
-  **ops**: Operational updates (deployment, backup, recovery, …)
-  **chore**: Miscellaneous commits (.gitignore, …)

Version Tags and Incrementing Version Numbers
---------------------------------------------

We follow `Semantic Versioning <https://semver.org/>`__ for versioning
our releases. The version number is composed of three parts:
``MAJOR.MINOR.PATCH``.

-  **MAJOR**: Increment when you make incompatible API changes.
-  **MINOR**: Increment when you add functionality in a
   backward-compatible manner.
-  **PATCH**: Increment when you make backward-compatible bug fixes.

Explanation
~~~~~~~~~~~

-  **Initial release**: ``1.0.0``
-  **Backward-compatible feature addition**: ``1.1.0``
-  **Backward-compatible bug fix**: ``1.1.1``
-  **Incompatible API change**: ``2.0.0``

Git Command Tips
----------------

-  **Check Current Branch**:

   .. code:: bash

      git branch

-  **Create a New Branch**:

   .. code:: bash

      git checkout -b branch-name

-  **Stage Changes for Commit**:

   .. code:: bash

      git add .

-  **Commit Changes**:

   .. code:: bash

      git commit -m "your commit message"

-  **Push Branch to Remote**:

   .. code:: bash

      git push origin branch-name

-  **Update Local Main Branch**:

   .. code:: bash

      git checkout main
      git pull origin main

-  **Merge Branch into Main**:

   .. code:: bash

      git checkout main
      git merge branch-name
      git push origin main

-  **Delete a Branch Locally**:

   .. code:: bash

      git branch -d branch-name

-  **Delete a Branch Remotely**:

   .. code:: bash

      git push origin --delete branch-name
