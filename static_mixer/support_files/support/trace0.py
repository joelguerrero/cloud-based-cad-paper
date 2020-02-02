 # trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
outlet_1000vtk = LegacyVTKReader(FileNames=['./VTK/outlet/outlet_1000.vtk'])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
renderView1.ViewSize = [800, 600]

# show data in view
outlet_1000vtkDisplay = Show(outlet_1000vtk, renderView1)

# trace defaults for the display properties.
outlet_1000vtkDisplay.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera()

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data
renderView1.ResetCamera()

# set scalar coloring
ColorBy(outlet_1000vtkDisplay, ('POINTS', 'U', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
outlet_1000vtkDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
outlet_1000vtkDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')

# get opacity transfer function/opacity map for 'U'
uPWF = GetOpacityTransferFunction('U')

# set scalar coloring
ColorBy(outlet_1000vtkDisplay, ('POINTS', 'U', 'Z'))

# rescale color and/or opacity maps used to exactly fit the current data range
outlet_1000vtkDisplay.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(uLUT, outlet_1000vtkDisplay)

# current camera placement for renderView1
renderView1.CameraPosition = [-4.3213367462158203e-07, 4.3213367462158203e-07, 2.731984611922754]
renderView1.CameraFocalPoint = [-4.3213367462158203e-07, 4.3213367462158203e-07, -5.5510989103857767e-17]
renderView1.CameraParallelScale = 0.7070896484926279


#Set background

# Properties modified on renderView1 - White background
#renderView1.Background = [1.0, 1.0, 1.0]

# Properties modified on renderView1 - Grey backgorund
renderView1.Background = [0.31999694819562063, 0.3400015259021897, 0.4299992370489052]


# save screenshot
SaveScreenshot('./fbar.png', renderView1, ImageResolution=[800, 600])

# hide color bar/color legend
outlet_1000vtkDisplay.SetScalarBarVisibility(renderView1, False)

# current camera placement for renderView1
renderView1.CameraPosition = [-4.3213367462158203e-07, 4.3213367462158203e-07, 2.731984611922754]
renderView1.CameraFocalPoint = [-4.3213367462158203e-07, 4.3213367462158203e-07, -5.5510989103857767e-17]
renderView1.CameraParallelScale = 0.7070896484926279

# save screenshot
SaveScreenshot('./fnobar.png', renderView1, ImageResolution=[800, 600])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-4.3213367462158203e-07, 4.3213367462158203e-07, 2.731984611922754]
renderView1.CameraFocalPoint = [-4.3213367462158203e-07, 4.3213367462158203e-07, -5.5510989103857767e-17]
renderView1.CameraParallelScale = 0.7070896484926279

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
