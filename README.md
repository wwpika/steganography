# steganography
python实现图片隐写
将文字信息藏在图片中，然后获取图片中隐藏的文字
 
原理：利用图片三个颜色分量（rgb）的最低有效位来隐藏信息（本程序隐藏的是文字）；
例如：11111111和11111110这两个值所表示的蓝色，人眼几乎无法区分，所以，该最低有效位可以用来存储颜色之外的信息，而且在某种程度上几乎是检测不到的


RGB32使用32位来表示一个像素，RGB分量各用去8位，剩下的8位用作Alpha通道或者不用。（ARGB32就是带Alpha通道的RGB24）
通常可以使用RGBQUAD数据结构来操作一个像素，它的定义为：
typedef struct tagRGBQUAD {
BYTE rgbBlue; // 蓝色分量
BYTE rgbGreen; // 绿色分量
BYTE rgbRed; // 红色分量
BYTE rgbReserved; // 保留字节（用作Alpha通道或忽略）
} RGBQUAD。

注意 ：有的图片的像素值为(r,g,b,t)，有的为(r,g,b)，可以根据实际情况来修改代码