function denoisedI = denoise(pathname)
    net = denoisingNetwork("DnCNN");
    I = imread(pathname);
    denoisedI = denoiseImage(I,net);
    imshow(denoisedI)
end