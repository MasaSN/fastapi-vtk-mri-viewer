# First access the VTK module (and any other needed modules) by importing them.
# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkConeSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderer
)

def main(argv):
    # to select the color of the object and the background
    colors = vtkNamedColors()

    # now we create an instance of the cone that we want to vizualize
    # which is part of the processing pipeline as well
    cone = vtkConeSource()
    cone.SetHeight(3.0)
    cone.SetRadius(1.0)
    cone.SetResolution(10)

    # in this step we will set the mapper and end the pipeline as it will recieve 
    # information from the Source and prepare it for rendering
    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection(cone.GetOutputPort())

    # the actor is responsible of controling how the mapper represent the 3d data
    coneActor = vtkActor()
    coneActor.SetMapper(coneMapper)
    coneActor.GetProperty().SetColor(colors.GetColor3d('MistyRose'))

    # now we will create the renderers and assign actors to it
    ren1 = vtkRenderer()
    ren1.AddActor(coneActor)
    ren1.SetBackground(colors.GetColor3d('MidnightBlue'))

    # at the end we will create the render window which will show 
    # up on the screen 
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren1)
    renWin.SetSize(300,300)
    renWin.SetWindowName('first_project')

    # Now we loop over 360 degrees and render the cone each time.
    for i in range(0, 360):
            # Render the image
            renWin.Render()
            # Rotate the active camera by one degree.
            ren1.GetActiveCamera().Azimuth(1)

if __name__ == '__main__':
    import sys

    main(sys.argv)