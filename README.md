# BNotebooks

A Blender add-on that enables the use of Blender as a kernel for Jupyter Notebooks.

This is a repackaging of [`blender_notebook`](https://github.com/cheng-chi/blender_notebook), but as an installable Blender add-on. Packaging it as an add-on removes the need for another python environment for installation, and keeps Blender's bundled python environment more isolated for better reproducibility.

## Installation

Download the [latest release](https://github.com/BradyAJohnston/BNotebooks/releases/latest) of `BNotebooks_X.zip` from github release.

Install the `BNotebooks_X.zip` via the `Addons` tab in the `Preferences`.

`Blender Prefernces` -> `Add-ons` -> `Install` 

Select the `BNotebooks_X.zip`. Click the top left tick box to enable the addon, which will display the add-on preferences. Click the `Install jupyterlab` button to install the required package.

Don't panic! If you encounter an error (`pkg_resources.ContextualVersionConflict`), it may be due to a newer version of the requests library being installed. To resolve this issue, simply **close and reopen your Blender application**. Then, navigate to the "Addons" tab, search for "BNotebooks," and proceed with the following actions.

Click `Append Kernel` to register this Blender as a kernel for use in Jupyter Notebooks.

![](https://i.imgur.com/FcB230V.png)

**This Blender version will now be available as a jupyter kernel.**

## Usage

Open a Jupyter notebook within Jupyter Lab (or VSCode), and upon selecting the "blender_x" kernel, an associated Blender instance should automatically launch. Verify the connection by executing the command `import bpy`. Please note that the Blender session will become unresponsive while a Python command is executing.

![](https://i.imgur.com/w77dUt0.png)

Keep in mind that when you close Blender, the associated kernel will also be shut down, and vice versa. For more information on how to use the Blender Python API, you can refer to the official [Blender Python API documentation](https://docs.blender.org/api/current/index.html).
