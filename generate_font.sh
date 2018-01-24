#!/bin/bash
prefix="qlalpha"
# 生成字符特征文件
sudo tesseract eng.$prefix.exp0.tif eng.$prefix.exp0 nobatch box.train
# 产生字符集
sudo unicharset_extractor eng.$prefix.exp0.box
# 生成shapetable
sudo shapeclustering -F font_properties -U unicharset eng.$prefix.exp0.tr
# 聚集字符特征
sudo mftraining -F font_properties -U unicharset eng.$prefix.exp0.tr
# 生成字符形状正常变化特征文件normproto
sudo cntraining eng.$prefix.exp0.tr
# 给inttemp,normproto,pffmtable,shapetable,unicharset 添加前缀 “jc001.”,也就是我们的字体名。
mv unicharset $prefix.unicharset
mv shapetable $prefix.shapetable
mv pffmtable $prefix.pffmtable
mv normproto $prefix.normproto
mv inttemp $prefix.inttemp
# 生成语言库
sudo combine_tessdata $prefix.
