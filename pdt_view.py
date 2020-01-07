# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENCE BLOCK *****
#
# -----------------------------------------------------------------------
# Author: Alan Odom (Clockmender), Rune Morling (ermo) Copyright (c) 2019
#
# Contains code which was inspired by the "Reset 3D View" plugin authored
# by Reiner Prokein (tiles) Copyright (c) 2014 (see T37718)
# -----------------------------------------------------------------------
#
import bpy
from bpy.types import Operator
from math import pi
from mathutils import Quaternion
from .pdt_functions import debug, euler_to_quaternion
from .pdt_menus import PDT_PT_PanelViewControl

# Runs when operator's tooltip is triggered
def highlight(ui_group, redraw):
    ui_groups = PDT_PT_PanelViewControl._ui_groups

    # Highlight
    ui_groups[ui_group] = True
    redraw()

    def set_false():
        ui_groups[ui_group] = False
        redraw()

    bpy.app.timers.register(set_false, first_interval=2.0)

class PDT_OT_ViewRot(Operator):
    bl_idname = "pdt.viewrot"
    bl_label = "Rotate View"
    bl_options = {"REGISTER", "UNDO"}
    bl_description = "View Rotation by Absolute Values"

    ui_group: bpy.props.IntProperty(
        default=-1, options={'HIDDEN', 'SKIP_SAVE'})

    @classmethod
    def description(cls, context, self):
        if self.ui_group != -1:
            redraw = context.area.tag_redraw
            highlight(self.ui_group, redraw)
        return cls.bl_description

    def execute(self, context):
        """View Rotation by Absolute Values.

        Rotations are converted to 3x3 Quaternion Rotation Matrix.
        This is an Absolute Rotation, not an Incremental Orbit.

        Args:
            context: Blender bpy.context instance.

        Notes:
            Uses pg.rotation_coords scene variables

        Returns:
            Status Set.
        """

        scene = context.scene
        pg = scene.pdt_pg
        areas = [a for a in context.screen.areas if a.type == "VIEW_3D"]
        if len(areas) > 0:
            roll_value = euler_to_quaternion(
                pg.rotation_coords.x * pi / 180,
                pg.rotation_coords.y * pi / 180,
                pg.rotation_coords.z * pi / 180
            )
            areas[0].spaces.active.region_3d.view_rotation = roll_value
        return {"FINISHED"}


class PDT_OT_vRotL(Operator):
    bl_idname = "pdt.viewleft"
    bl_label = "Rotate Left"
    bl_options = {"REGISTER", "UNDO"}
    bl_description = "View Orbit Left by Delta Value"

    ui_group: bpy.props.IntProperty(
        default=-1, options={'HIDDEN', 'SKIP_SAVE'})

    @classmethod
    def description(cls, context, self):
        if self.ui_group != -1:
            redraw = context.area.tag_redraw
            highlight(self.ui_group, redraw)
        return cls.bl_description

    def execute(self, context):
        """View Orbit Left by Delta Value.

        Orbits view to the left about its vertical axis

        Args:
            context: Blender bpy.context instance.

        Notes:
            Uses pg.vrotangle scene variable

        Returns: Status Set.
        """

        scene = context.scene
        pg = scene.pdt_pg
        areas = [a for a in context.screen.areas if a.type == "VIEW_3D"]
        if len(areas) > 0:
            bpy.ops.view3d.view_orbit(angle=(pg.vrotangle * pi / 180), type="ORBITLEFT")
        return {"FINISHED"}


class PDT_OT_vRotR(Operator):
    bl_idname = "pdt.viewright"
    bl_label = "Rotate Right"
    bl_options = {"REGISTER", "UNDO"}
    bl_description = "View Orbit Right by Delta Value"

    ui_group: bpy.props.IntProperty(
        default=-1, options={'HIDDEN', 'SKIP_SAVE'})

    @classmethod
    def description(cls, context, self):
        if self.ui_group != -1:
            redraw = context.area.tag_redraw
            highlight(self.ui_group, redraw)
        return cls.bl_description

    def execute(self, context):
        """View Orbit Right by Delta Value.

        Orbits view to the right about its vertical axis

        Args:
            context: Blender bpy.context instance.

        Notes:
            Uses pg.vrotangle scene variable

        Returns:
            Status Set.
        """

        scene = context.scene
        pg = scene.pdt_pg
        areas = [a for a in context.screen.areas if a.type == "VIEW_3D"]
        if len(areas) > 0:
            bpy.ops.view3d.view_orbit(angle=(pg.vrotangle * pi / 180), type="ORBITRIGHT")
        return {"FINISHED"}


class PDT_OT_vRotU(Operator):
    bl_idname = "pdt.viewup"
    bl_label = "Rotate Up"
    bl_options = {"REGISTER", "UNDO"}
    bl_description = "View Orbit Up by Delta Value"

    ui_group: bpy.props.IntProperty(
        default=-1, options={'HIDDEN', 'SKIP_SAVE'})

    @classmethod
    def description(cls, context, self):
        if self.ui_group != -1:
            redraw = context.area.tag_redraw
            highlight(self.ui_group, redraw)
        return cls.bl_description

    def execute(self, context):
        """View Orbit Up by Delta Value.

        Orbits view up about its horizontal axis

        Args:
            context: Blender bpy.context instance.

        Notes:
            Uses pg.vrotangle scene variable

        Returns:
            Status Set.
        """

        scene = context.scene
        pg = scene.pdt_pg
        areas = [a for a in context.screen.areas if a.type == "VIEW_3D"]
        if len(areas) > 0:
            bpy.ops.view3d.view_orbit(angle=(pg.vrotangle * pi / 180), type="ORBITUP")
        return {"FINISHED"}


class PDT_OT_vRotD(Operator):
    bl_idname = "pdt.viewdown"
    bl_label = "Rotate Down"
    bl_options = {"REGISTER", "UNDO"}
    bl_description = "View Orbit Down by Delta Value"

    ui_group: bpy.props.IntProperty(
        default=-1, options={'HIDDEN', 'SKIP_SAVE'})

    @classmethod
    def description(cls, context, self):
        if self.ui_group != -1:
            redraw = context.area.tag_redraw
            highlight(self.ui_group, redraw)
        return cls.bl_description

    def execute(self, context):
        """View Orbit Down by Delta Value.

        Orbits view down about its horizontal axis

        Args:
            context: Blender bpy.context instance.

        Notes:
            Uses pg.vrotangle scene variable

        Returns:
            Status Set.
        """

        scene = context.scene
        pg = scene.pdt_pg
        areas = [a for a in context.screen.areas if a.type == "VIEW_3D"]
        if len(areas) > 0:
            bpy.ops.view3d.view_orbit(angle=(pg.vrotangle * pi / 180), type="ORBITDOWN")
        return {"FINISHED"}


class PDT_OT_vRoll(Operator):
    bl_idname = "pdt.viewroll"
    bl_label = "Roll View"
    bl_options = {"REGISTER", "UNDO"}
    bl_description = "View Roll by Delta Value"

    ui_group: bpy.props.IntProperty(
        default=-1, options={'HIDDEN', 'SKIP_SAVE'})

    @classmethod
    def description(cls, context, self):
        if self.ui_group != -1:
            redraw = context.area.tag_redraw
            highlight(self.ui_group, redraw)
        return cls.bl_description

    def execute(self, context):
        """View Roll by Delta Value.

        Rolls view about its normal axis

        Args:
            context: Blender bpy.context instance.

        Notes:
            Uses pg.vrotangle scene variable

        Returns:
            Status Set.
        """

        scene = context.scene
        pg = scene.pdt_pg
        areas = [a for a in context.screen.areas if a.type == "VIEW_3D"]
        if len(areas) > 0:
            bpy.ops.view3d.view_roll(angle=(pg.vrotangle * pi / 180), type="ANGLE")
        return {"FINISHED"}


class PDT_OT_viso(Operator):
    """Isometric View."""

    bl_idname = "pdt.viewiso"
    bl_label = "Isometric View"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        """Set Isometric View.

        Set view orientation to Isometric

        Args:
            context: Blender bpy.context instance.

        Returns:
            Status Set.
        """

        areas = [a for a in context.screen.areas if a.type == "VIEW_3D"]
        if len(areas) > 0:
            # Try working this out in your head!
            areas[0].spaces.active.region_3d.view_rotation = Quaternion(
                (0.8205, 0.4247, -0.1759, -0.3399)
            )
        return {"FINISHED"}


class PDT_OT_Reset3DView(Operator):
    """Reset 3D View to Blender Defaults."""

    bl_idname = "pdt.reset_3d_view"
    bl_label = "Reset 3D View"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        """Reset 3D View to Blender Defaults.

        Args:
            context: Blender bpy.context instance.

        Returns:
            Status Set.
        """

        # The default view_distance to the origin when starting up Blender
        default_view_distance = 17.986562728881836
        # The default view_matrix when starting up Blender
        default_view_matrix = (
            (0.41, -0.4017, 0.8188, 0.0),
            (0.912, 0.1936, -0.3617, 0.0),
            (-0.0133, 0.8950, 0.4458, 0.0),
            (0.0, 0.0, -17.9866, 1.0)
        )

        for area in (a for a in context.screen.areas if a.type == 'VIEW_3D'):
            view = area.spaces[0].region_3d
            if view is not None:
                debug(f"is_orthographic_side_view: {view.is_orthographic_side_view}")
                if view.is_orthographic_side_view:
                    # When the view is orthographic, reset the distance and location.
                    # The rotation already fits.
                    debug(f"view_distance before reset: {view.view_distance}")
                    debug(f"view_location before reset: {view.view_location}")
                    view.view_distance = default_view_distance
                    view.view_location = (-0.0, -0.0, -0.0)
                    view.update()
                    debug(f"view_distance AFTER reset: {view.view_distance}")
                    debug(f"view_location AFTER reset: {view.view_location}")
                else:
                    # Otherwise, the view matrix needs to be reset (includes distance).
                    debug(f"view_matrix before reset:\n{view.view_matrix}")
                    view.view_matrix = default_view_matrix
                    view.update()
                    debug(f"view_matrix AFTER reset:\n{view.view_matrix}")

        return {'FINISHED'}
