pristineRGB = imread("lighthouse.png");
pristineRGB = im2double(pristineRGB);
imshow(pristineRGB)
title("Pristine Image")

noisyRGB = imnoise(pristineRGB,"gaussian",0,0.01);
imshow(noisyRGB)
title("Noisy Image")

% [noisyR,noisyG,noisyB] = imsplit(noisyRGB);
% 
% net = denoisingNetwork("dncnn");
% 
% denoisedR = denoiseImage(noisyR,net);
% denoisedG = denoiseImage(noisyG,net);
% denoisedB = denoiseImage(noisyB,net);
% 
% denoisedRGB = cat(3,denoisedR,denoisedG,denoisedB);
% imshow(denoisedRGB)
% title("Denoised Image")