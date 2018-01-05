#!/usr/bin/env python
import pyqtgraph as pg
import numpy as np
pg.mkQApp()
import pyqtgraph.opengl as gl
view = gl.GLViewWidget()
view.show()

xgrid = gl.GLGridItem()
ygrid = gl.GLGridItem()
zgrid = gl.GLGridItem()

# view.addItem(xgrid)
# view.addItem(ygrid)
view.addItem(zgrid)

xgrid.rotate(90, 0, 1, 0)
ygrid.rotate(90, 1, 0, 0)

xgrid.scale(0.2, 0.1, 0.1)
ygrid.scale(0.2, 0.1, 0.1)
zgrid.scale(0.2, 0.2, 0.2)

coords = np.array([[0.1, 0.1, 0.1]])
colors = (1, 1, 1, 1)
plt = gl.GLScatterPlotItem(pos=coords, color = colors, size=5, pxMode=True)
view.addItem(plt)
