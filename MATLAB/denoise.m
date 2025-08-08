function denoisedI = denoise(pathname)
    net = denoisingNetwork("DnCNN");
    I = imread(pathname);
    denoisedI = denoiseImage(I,net);
    results = ocr(I);
    display(results);
end