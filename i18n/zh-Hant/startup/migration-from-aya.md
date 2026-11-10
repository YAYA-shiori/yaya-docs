# 從 AYA 移行

將既有的 AYA5 人格移行至 YAYA。

## 注意事項

### DLL 名稱變更

DLL 名稱會從 `aya5.dll` 變更為 `yaya.dll`。

- 因此，`aya5.txt` 必須重新命名為 `yaya.txt`
- 存檔檔名會變成 `yaya_variable.cfg`，存檔資料不會自動移行

為避免此情況，YAYA 提供了相關功能。開啟 `aya_shiori3.dic`，並在 `load` 函式的 `OnLoad` 前方加入以下程式碼。

```
if FSIZE('yaya_variable.cfg') <= 0 {
	RESTOREVAR('aya5_variable.cfg')
	SAVEVAR('yaya_variable.cfg')
	FDEL('aya5_variable.cfg')
}
```

如果沒有修改過 `aya_shiori3.dic`，只要參照[系統辭典](../system/yaya-shiori3-dic.md)的項目，下載所需檔案並覆寫，就能輕鬆完成移行（若要使用舊版相容辭典，請在 `yaya.txt` 中的 `aya_shiori3.dic` 後方，加入 AYA 相容用的辭典。目前的系統辭典中，對應的是 `compatible.dic`）。

### 系統辭典變更

系統辭典會有所變更（建議替換）。

- AYA5 的系統辭典會將 SAORI 的傳回值等內容中的位元組值 1 替換為逗號，並將數字轉換為數值，而非字串；YAYA 用的系統辭典預設不會進行這些處理
- 部分函式（例如 `NAMETOVALUE`）不包含在系統辭典中

## 移行步驟

以下說明**未修改 AYA5 的 `aya_shiori3.dic` 時**的移行步驟。以下所有作業都在該人格的辭典資料夾（`ghost/master/`）中進行。

1. 將 `descript.txt` 中的 `shiori,aya5.dll` 改寫為 `shiori,yaya.dll`
2. 刪除 `aya5.dll`，並放入 `yaya.dll`
3. 將 `aya5.txt` 重新命名為 `yaya.txt`
4. 下載[紺野ややめ](http://ms.shillest.net/yayame.xhtml)，將 NAR 檔案解壓縮為 ZIP，或安裝人格，讓你能查看其中的檔案
5. 參照[系統辭典](../system/yaya-shiori3-dic.md)，複製 `system` 資料夾及其下的內容
6. 複製 `system_config.txt`
7. 刪除 `yaya.txt` 內的 `dic,aya_shiori3.dic`，改為寫上 `include, system_config.txt`
8. 開啟 `config.dic`，將 `SHIORI3FW.AUTO_DATA_CONVERT` 設為 1，並將 `SHIORI3FW.REF_ACCEL` 設為 0

完成以上作業後，大部分移行相關錯誤都會消除。

## 網路散布時

透過網路散布時，`aya5.dll` 和 `aya5.txt` 已不再需要，建議使用內容如下的 `delete.txt` 等檔案將它們刪除。

```
ghost/master/aya5.dll
ghost/master/aya5.txt
```

## 相關

- [使用 YAYA 製作人格](./creating-ghost.md)
- [系統辭典/yaya_shiori3.dic](../system/yaya-shiori3-dic.md)
