# Connected Component Labelling

Connected components labeling scans an image and groups its pixels into components based on pixel connectivity, all pixels in a connected component share similar pixel intensity values and are in some way connected with each other. Once all groups have been determined, each pixel is labeled with a graylevel or a color (color labeling) according to the component it was assigned to.
Extracting and labeling of various disjoint and connected components in an image is central to many automated image analysis applications.

# How It Works

Connected component labeling works by scanning an image, pixel-by-pixel (from top to bottom and left to right) in order to identify connected pixel regions, regions of adjacent pixels which share the same set of intensity values V. (For a binary image V={1}; however, in a graylevel image V will take on a range of values, for example: V={51, 52, 53, ..., 77, 78, 79, 80}.)

Connected component labeling works on binary or graylevel images and different measures of connectivity are possible. However, for the following we assume binary input images and 8-connectivity. The connected components labeling operator scans the image by moving along a row until it comes to a point p (where p denotes the pixel to be labeled at any stage in the scanning process) for which V={1}. When this is true, it examines the four neighbors of p which have already been encountered in the scan (the neighbors (i) to the left of p, (ii) above it, and (iii and iv) the two upper diagonal terms). Based on this information, the labeling of p occurs as follows:

·If all four neighbors are 0, assign a new label to p, else
·if only one neighbor has V={1}, assign its label to p, else
·if more than one of the neighbors have V={1}, assign one of the labels to p and make a note of the equivalences.
After completing the scan, the equivalent label pairs are sorted into equivalence classes and a unique label is assigned to each class. As a final step, a second scan is made through the image, during which each label is replaced by the label assigned to its equivalence classes. For display, the labels might be different graylevels or colors.

# Bağlı Bileşen Etiketleme Yöntemi
Bağlı Bileşen Etiketleme Yöntemi, ikili(siyah-beyaz) görüntüyü tarayarak birbiriyle bağlntılı olan pikselleri aynı etiket değerleri ile etiketleyen bir Nesne Etiketleme yöntemidir. Bu etiketleme işlemi ile görüntülerdeki nesnelerin konumları tespit edilmiş olur. Hatta konumları tespit edilen bileşenler birbirlerinin 
dikdörtgensel alanına girmiş olsalar bile ayrı ayrı başka görüntülere aktarılabilir ve nesne tespiti için kolaylık sağlar. Bu yöntem için birçok algoritma bulunmaktadır. Örneğin: 
