def mean_filt(inp_img1):
  for x in range(1, inp_img.shape[0]-1):
      for y in range(1, inp_img.shape[1]-1):
        
          #we use 3x3 kernel window for the mean filter
          total = 0.0
          total = total + inp_img1[x,y]        #centre pixel
          total = total + inp_img1[x-1,y]      #left
          total = total + inp_img1[x-1,y+1]    #bottom left
          total = total + inp_img1[x,y+1]      #bottom
          total = total + inp_img1[x+1,y+1]    #bottom right
          total = total + inp_img1[x+1,y]      #right
          total = total + inp_img1[x+1,y-1]    #top right
          total = total + inp_img1[x,y-1]      #top
          total = total + inp_img1[x-1,y-1]    #top left
        
          inp_img1[x,y] = int(total/9)        #average of all the pixels in the 3x3 kernel window
          
 return inp_img1
 
 def add_sp_noise(image, percent_noise):
    if(percent_noise >50):    #if noise exceeds 50%, its very troublesome to de-noise it
        return -1
    
    pixel_count = 0
    
    while(True):
        for x in range(0, image.shape[0]):
            for y in range(0, image.shape[1]):
                
                mode = random.randrange(0,50)
                
                if (mode == 1):         #salt pixel adding
                    #salt pixels to be added
                    image[x,y] = 255
                    pixel_count = pixel_count + 1
                    
                if (mode == 9):         #pepper pixel adding
                    #pepper pixels to be added
                    image[x,y] = 0
                    pixel_count = pixel_count + 1
  
                if pixel_count > ((image.shape[0] * image.shape[1]) * percent_noise / 100) : 
                    #percentage of noise in the image can be calculted by 
                    #the number of noise pixels and total pixels in the image
                    
                    return image
                
 def median_filt(inp_img1):
    
    for x in range(1, inp_img1.shape[0]-1):
        for y in range(1, inp_img1.shape[1]-1):
            
            #we use 3x3 window for median filter
            kernel_mat = np.zeros(9)
                
            kernel_mat[0] = inp_img1[x,y]        #centre pixel
            kernel_mat[1] = inp_img1[x-1,y]      #left
            kernel_mat[2] = inp_img1[x-1,y+1]    #bottom left
            kernel_mat[3] = inp_img1[x,y+1]      #bottom
            kernel_mat[4] = inp_img1[x+1,y+1]    #bottom right
            kernel_mat[5] = inp_img1[x+1,y]      #right
            kernel_mat[6] = inp_img1[x+1,y-1]    #top right
            kernel_mat[7] = inp_img1[x,y-1]      #top
            kernel_mat[8] = inp_img1[x-1,y-1]    #top left
                
            inp_img1[x,y] = np.median(kernel_mat)
                
    return inp_img1
                
 def gaussian_filt(inp_img1):
    for x in range(1, inp_img.shape[0]-1):
      for y in range(1, inp_img.shape[1]-1):
        
          #we use 3x3 kernel window for the mean filter
          total = 0.0
          total = total + (inp_img1[x,y] * 0.76)         #centre pixel
          total = total + (inp_img1[x-1,y] * 0.25)      #left
          total = total + (inp_img1[x-1,y+1] * 0.071)   #bottom left
          total = total + (inp_img1[x,y+1] * 0.25)      #bottom
          total = total + (inp_img1[x+1,y+1] * 0.071)   #bottom right
          total = total + (inp_img1[x+1,y] * 0.25)      #right
          total = total + (inp_img1[x+1,y-1] * 0.071)   #top right
          total = total + (inp_img1[x,y-1] * 0.25)      #top
          total = total + (inp_img1[x-1,y-1] * 0.071)   #top left
        
          inp_img1[x,y] = int(total/2.044)              #average of all the pixels in the 3x3 kernel window
          
     return inp_img1
                    
