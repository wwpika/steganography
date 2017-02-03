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

bin():Convert an integer number to a binary string.

Image.getdata():Returns the contents of this image as a sequence object containing pixel values.

Image.putdata():Copies pixel data to this image.

Image.new():Creates a new image with the given mode and size.f-8

注意：

1.将藏在图片中的数据提取出来后，需要对其进行解码，然后将它转换为字符串，在次之前，要先了解utf-8的编码方式(不同的字符占用的字节数不一样)

对于UTF-8编码中的任意字节B，如果B的第一位为0，则B独立的表示一个字符(ASCII码)；

如果B的第一位为1，第二位为0，则B为一个多字节字符中的一个字节(非ASCII字符)；

如果B的前两位为1，第三位为0，则B为两个字节表示的字符中的第一个字节；

如果B的前三位为1，第四位为0，则B为三个字节表示的字符中的第一个字节；

如果B的前四位为1，第五位为0，则B为四个字节表示的字符中的第一个字节；
