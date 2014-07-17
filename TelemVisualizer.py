def telemvisualizer(subdirectory,filenum,save=False):
    '''
    Visualizes slopes, intensities, and newpos data in a heatmap grid, and 
    plots tip/tilt and pinned actuators as a function of time.
    Inputs: subdirectory & filenum = strings, save = optional boolean
    Outputs: 6 figures, 4 with the heatmap grids and 2 plots as a function of time
    '''
    
    
    from matplotlib import pyplot as plt
    import numpy as np
    
    from kapaolibplus import (subaps_to_grid, overlay_indices, Slopes, IntensityMap, DMPositions, newpos_to_grid, overlay_indices_newpos, slope_to_grid, overlay_indices_slope)
        
    
    SLOPE_X_FILE = './' + subdirectory + '/' + 'slope_x_' + filenum + '.tel'
    SLOPE_Y_FILE = './' + subdirectory + '/' + 'slope_y_' + filenum + '.tel'
    INTENSITY_MAP = './' + subdirectory + '/' + 'intensity_map_' + filenum + '.tel'
    NEWPOS_FILE = './' + subdirectory + '/' + 'new_pos_' + filenum + '.tel'
    
    slope_x, slope_y, intensity_map = Slopes(SLOPE_X_FILE), Slopes(SLOPE_Y_FILE), IntensityMap(INTENSITY_MAP)
    new_pos = DMPositions(NEWPOS_FILE)
    
    
    
    length = len(slope_x.data)
    
    
    #finding min and max values at each of the 3 relevant time steps, then the overall min and max values between the 3
    
    # X slope
    xmin_t0 = min(slope_x.data[0])
    xmin_mid = min(slope_x.data[int(length/2)])
    xmin_last = min(slope_x.data[length - 1])
    xmax_t0 = max(slope_x.data[0])
    xmax_mid = max(slope_x.data[int(length/2)])
    xmax_last = max(slope_x.data[length - 1])
    
    xmin = min(xmin_t0,xmin_mid,xmin_last)
    xmax = max(xmax_t0,xmax_mid,xmax_last)
    
    
    # Y slope
    
    ymin_t0 = min(slope_y.data[0])
    ymin_mid = min(slope_y.data[int(length/2)])
    ymin_last = min(slope_y.data[length - 1])
    ymax_t0 = max(slope_y.data[0])
    ymax_mid = max(slope_y.data[int(length/2)])
    ymax_last = max(slope_y.data[length - 1])
    
    ymin = min(ymin_t0,ymin_mid,ymin_last)
    ymax = max(ymax_t0,ymax_mid,ymax_last)
    
    
    # Intensities
    
    intensmin_t0 = min(intensity_map.data[0])
    intensmin_mid = min(intensity_map.data[int(length/2)])
    intensmin_last = min(intensity_map.data[length - 1])
    intensmax_t0 = max(intensity_map.data[0])
    intensmax_mid = max(intensity_map.data[int(length/2)])
    intensmax_last = max(intensity_map.data[length - 1])
    
    intensmin = min(intensmin_t0,intensmin_mid,intensmin_last)
    intensmax = max(intensmax_t0,intensmax_mid,intensmax_last)
    
    
    # Newpos
    
    newposshort_t0 = np.zeros(120)
    newposshort_mid = np.zeros(120)
    newposshort_last = np.zeros(120)
    
    for i in range(120):
        newposshort_t0[i] = new_pos.data[0][i]
        newposshort_mid[i] = new_pos.data[int(length/2)][i]
        newposshort_last[i] = new_pos.data[length - 1][i]
        
    newposmin_t0 = min(newposshort_t0)
    newposmin_mid = min(newposshort_mid)
    newposmin_last = min(newposshort_last)
    newposmax_t0 = max(newposshort_t0)
    newposmax_mid = max(newposshort_mid)
    newposmax_last = max(newposshort_last)
    
    newposmin = min(newposmin_t0,newposmin_mid,newposmin_last)
    newposmax = max(newposmax_t0,newposmax_mid,newposmax_last)
    
    
    
    # Plots
    
    
    # X Slope
        
    figx = plt.figure(figsize=(20,10))
    plt.subplot(241)
    plt.imshow(slope_to_grid(slope_x.data[0]), origin='lower',vmin = xmin, vmax = xmax)
    overlay_indices_slope()
    plt.colorbar()
    plt.title('first time step')
    
    plt.subplot(242)
    plt.imshow(slope_to_grid(slope_x.data[int(length/2)]), origin='lower',vmin = xmin, vmax = xmax)
    overlay_indices_slope()
    plt.colorbar()
    plt.title('middle time step')
    
    plt.subplot(243)
    plt.imshow(slope_to_grid(slope_x.data[length-1]), origin='lower',vmin = xmin, vmax = xmax)
    overlay_indices_slope()
    plt.colorbar()
    plt.title('last time step')
    
    plt.subplot(244)
    plt.imshow(slope_to_grid(slope_x.median_by_slope), origin='lower',vmin = xmin, vmax = xmax)
    overlay_indices()
    plt.colorbar()
    plt.title('median slopes')
    
        
    plt.subplot(245)
    plt.imshow(slope_to_grid(slope_x.data[0]), origin='lower')
    overlay_indices_slope()
    plt.colorbar()
    plt.title('first time step')
    
    plt.subplot(246)
    plt.imshow(slope_to_grid(slope_x.data[int(length/2)]), origin='lower')
    overlay_indices_slope()
    plt.colorbar()
    plt.title('middle time step')
    
    plt.subplot(247)
    plt.imshow(slope_to_grid(slope_x.data[length-1]), origin='lower')
    overlay_indices_slope()
    plt.colorbar()
    plt.title('last time step')
    
    plt.subplot(248)
    plt.imshow(slope_to_grid(slope_x.median_by_slope), origin='lower')
    overlay_indices()
    plt.colorbar()
    plt.title('median slopes')
    
    plt.suptitle('X Slope Maps, Fixed and Unfixed',fontsize=16)
    

    
    # Y Slope
        
    figy = plt.figure(figsize=(20,10))
    plt.subplot(241)
    plt.imshow(slope_to_grid(slope_y.data[0]), origin='lower',vmin = ymin, vmax = ymax)
    overlay_indices_slope()
    plt.colorbar()
    plt.title('first time step')
    
    plt.subplot(242)
    plt.imshow(slope_to_grid(slope_y.data[int(length/2)]), origin='lower',vmin = ymin, vmax = ymax)
    overlay_indices_slope()
    plt.colorbar()
    plt.title('middle time step')
    
    plt.subplot(243)
    plt.imshow(slope_to_grid(slope_y.data[length-1]), origin='lower',vmin = ymin, vmax = ymax)
    overlay_indices_slope()
    plt.colorbar()
    plt.title('last time step')
    
    plt.subplot(244)
    plt.imshow(slope_to_grid(slope_y.median_by_slope), origin='lower',vmin = ymin, vmax = ymax)
    overlay_indices()
    plt.colorbar()
    plt.title('median slopes')
    
    
    
        
    plt.subplot(245)
    plt.imshow(slope_to_grid(slope_y.data[0]), origin='lower')
    overlay_indices_slope()
    plt.colorbar()
    plt.title('first time step')
    
    plt.subplot(246)
    plt.imshow(slope_to_grid(slope_y.data[int(length/2)]), origin='lower')
    overlay_indices_slope()
    plt.colorbar()
    plt.title('middle time step')
    
    plt.subplot(247)
    plt.imshow(slope_to_grid(slope_y.data[length-1]), origin='lower')
    overlay_indices_slope()
    plt.colorbar()
    plt.title('last time step')
    
    plt.subplot(248)
    plt.imshow(slope_to_grid(slope_y.median_by_slope), origin='lower')
    overlay_indices()
    plt.colorbar()
    plt.title('median slopes')
    
    plt.suptitle('Y Slope Maps, Fixed and Unfixed',fontsize=16)
    

    
    # Intensity
        
    figint = plt.figure(figsize=(20,10))
    plt.subplot(241)
    plt.imshow(subaps_to_grid(intensity_map.data[0]), origin='lower',vmin = intensmin, vmax = intensmax)
    overlay_indices()
    plt.colorbar()
    plt.title('first time step')
    
    plt.subplot(242)
    plt.imshow(subaps_to_grid(intensity_map.data[int(length/2)]), origin='lower',vmin = intensmin, vmax = intensmax)
    overlay_indices()
    plt.colorbar()
    plt.title('middle time step')
    
    plt.subplot(243)
    plt.imshow(subaps_to_grid(intensity_map.data[length-1]), origin='lower',vmin = intensmin, vmax = intensmax)
    overlay_indices()
    plt.colorbar()
    plt.title('last time step')
    
    plt.subplot(244)
    plt.imshow(subaps_to_grid(intensity_map.median_by_subap), origin='lower',vmin = intensmin, vmax = intensmax)
    overlay_indices()
    plt.colorbar()
    plt.title('median intensity')
    
    
    
        
    plt.subplot(245)
    plt.imshow(subaps_to_grid(intensity_map.data[0]), origin='lower')
    overlay_indices()
    plt.colorbar()
    plt.title('first time step')
    
    plt.subplot(246)
    plt.imshow(subaps_to_grid(intensity_map.data[int(length/2)]), origin='lower')
    overlay_indices()
    plt.colorbar()
    plt.title('middle time step')
    
    plt.subplot(247)
    plt.imshow(subaps_to_grid(intensity_map.data[length-1]), origin='lower')
    overlay_indices()
    plt.colorbar()
    plt.title('last time step')
    
    plt.subplot(248)
    plt.imshow(subaps_to_grid(intensity_map.median_by_subap), origin='lower')
    overlay_indices()
    plt.colorbar()
    plt.title('median intensity')
    
    plt.suptitle('Intensity Maps, Fixed and Unfixed',fontsize=16)
    

    
    
    # New Pos
        
    fignp = plt.figure(figsize=(20,10))
    plt.subplot(241)
    plt.imshow(newpos_to_grid(new_pos.data[0]), origin='lower',vmin = newposmin, vmax = newposmax)
    overlay_indices_newpos()
    plt.colorbar()
    plt.title('first time step')
    
    plt.subplot(242)
    plt.imshow(newpos_to_grid(new_pos.data[int(length/2)]), origin='lower',vmin = newposmin, vmax = newposmax)
    overlay_indices_newpos()
    plt.colorbar()
    plt.title('middle time step')
    
    plt.subplot(243)
    plt.imshow(newpos_to_grid(new_pos.data[length-1]), origin='lower',vmin = newposmin, vmax = newposmax)
    overlay_indices_newpos()
    plt.colorbar()
    plt.title('last time step')
    
    plt.subplot(244)
    plt.imshow(newpos_to_grid(new_pos.median_by_pos), origin='lower',vmin = newposmin, vmax = newposmax)
    overlay_indices_newpos()
    plt.colorbar()
    plt.title('median positions')
    
    
        
    plt.subplot(245)
    plt.imshow(newpos_to_grid(new_pos.data[0]), origin='lower')
    overlay_indices_newpos()
    plt.colorbar()
    plt.title('first time step')
    
    plt.subplot(246)
    plt.imshow(newpos_to_grid(new_pos.data[int(length/2)]), origin='lower')
    overlay_indices_newpos()
    plt.colorbar()
    plt.title('middle time step')
    
    plt.subplot(247)
    plt.imshow(newpos_to_grid(new_pos.data[length-1]), origin='lower')
    overlay_indices_newpos()
    plt.colorbar()
    plt.title('last time step')
    
    plt.subplot(248)
    plt.imshow(newpos_to_grid(new_pos.median_by_pos), origin='lower')
    overlay_indices_newpos()
    plt.colorbar()
    plt.title('median positions')
    
    plt.suptitle('DM Position (New_Pos) Maps, Fixed and Unfixed',fontsize=16)


    
    
    #Tip/tilt as a function of time
    
    #pulling out the 120th and 122nd index for each time step
    tt_1 = np.zeros(length)
    tt_2 = np.zeros(length)
    for i in range(0,length):
        tt_1[i] = new_pos.data[i][120]
        tt_2[i] = new_pos.data[i][122]
        
    figtime = plt.figure(figsize=(12,9))
    plt.subplots_adjust(hspace=.5)
    plt.subplot(3,1,1)
    plt.plot(new_pos.timestamps - new_pos.timestamps[0],tt_1)
    plt.ylabel("Tip/tilt index 120")
    plt.title('Tip/Tilt as  Function of Time',fontsize=16)
    
    plt.subplot(3,1,2)
    plt.plot(new_pos.timestamps - new_pos.timestamps[0],tt_2)
    plt.ylabel("Tip/tilt index 122")
    plt.xlabel("Time (ms)")
    
    
    
    #pinned actuators as a function of time
    
    pinned = np.zeros(length)
    for i in range(0,length):
        for j in range(0,120):
            if new_pos.data[i][j] <= 100 or new_pos.data[i][j] >= 64900:
                pinned[i] = pinned[i] + 1
                
    plt.subplot(3,1,3)
    plt.plot(new_pos.timestamps - new_pos.timestamps[0],pinned)
    plt.ylabel("Number of pinned actuators")
    plt.xlabel("Time (ms)")
    plt.title("Pinned Actuators as a Function of Time",fontsize=16)
    
    if save == True:
        figtime.savefig('./' + subdirectory + '/' + 'fig_tt_pinned_' + filenum + '.png', dpi=300)   
        fignp.savefig('./' + subdirectory + '/' + 'fig_new_pos_' + filenum + '.png', dpi=300)
        figint.savefig('./' + subdirectory + '/' + 'fig_intensity_map_' + filenum + '.png', dpi=300)    
        figy.savefig('./' + subdirectory + '/' + 'fig_slope_y_' + filenum + '.png', dpi=300)    
        figx.savefig('./' + subdirectory + '/' + 'fig_slope_x_' + filenum + '.png', dpi=300)
 
    
    
    plt.show()
