# WuCCD / 武昌号

## 中文 ## 
尽管叫当初叫做WuCCD，但这个图像传感器原理和CCD有很大差异，和CMOS更接近。
本程序是基于Waveshare High-Precision AD HAT驱动程序的修改。适用于树莓派5(Bookworm系统)，暂未在其它硬件上测试。
请按视频内容正确搭建设备，并安装matplotlib、lgpio和微雪提供的说明(https://www.waveshare.net/wiki/High-Precision_AD_HAT) 中的依赖项后，再运行WuCCD.py。运行程序时需遮盖光电二极管阵列，等待本底(Bias)拍摄完成后方可正常拍摄。
以下是Waveshare High-Precision AD HAT的Readme：
仅供原理演示，性能非常拉跨，无实际用途。

以下是Waveshare High-Precision AD HAT的Readme：
https://www.waveshare.net/shop/High-Precision-AD-HAT.htm
我是块Raspberry Pi扩展板，具备10通道32位高精度ADC和24位辅助ADC。
Raspberry Pi GPIO接口没有AD功能，如果你要用到高精度的ADC，那我将是不错的选择！

## English ## 
https://www.waveshare.com/18983.htm
I am a Raspberry Pi expansion board with an 10-channel 32-bit high-precision ADC and a 24-bit auxiliary ADC.
The Raspberry Pi GPIO interface does not have AD functionality. If you want to use high precision AD, then I will be a good choice!
