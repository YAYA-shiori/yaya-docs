# Migrating from AYA

Migrate an existing AYA5 ghost to YAYA.

## Notes

### DLL name change

The DLL name changes from `aya5.dll` to `yaya.dll`.

- Therefore, `aya5.txt` must be renamed to `yaya.txt`
- The save file name becomes `yaya_variable.cfg`, so save data is not migrated as-is
- If you started up using the AYA template, rename `aya5_variable.cfg` to `yaya_variable.cfg`

A feature is available to avoid this. Open `aya_shiori3.dic` and add the following code before `OnLoad` in the `load` function.

```
if FSIZE('yaya_variable.cfg') <= 0 {
	RESTOREVAR('aya5_variable.cfg')
	SAVEVAR('yaya_variable.cfg')
	FDEL('aya5_variable.cfg')
}
```

If you have not modified `aya_shiori3.dic`, you can migrate easily by downloading the required files and overwriting the existing ones, referring to the [system dictionary](../system/yaya-shiori3-dic.md) section (if you use the legacy compatibility dictionary, add the dictionary for AYA compatibility after `aya_shiori3.dic` in `yaya.txt`. In the current system dictionary, this is `compatible.dic`).

### System dictionary changes

The system dictionary changes (replacing it is recommended).

- In the AYA5 system dictionary, SAORI return values and similar values had byte value 1 replaced with a comma, and numbers were converted to numbers rather than strings. By default, the YAYA system dictionary does not perform these operations
- Some functions (such as `NAMETOVALUE`) are not included in the system dictionary

## Migration procedure

This section describes the migration procedure **for cases where `aya_shiori3.dic` has not been modified in AYA5**. Perform all of the following steps in the ghost's dictionary folder (`ghost/master/`).

1. In `descript.txt`, change `shiori,aya5.dll` to `shiori,yaya.dll`
2. Delete `aya5.dll` and place `yaya.dll` there
3. Rename `aya5.txt` to `yaya.txt`
4. Download [Konnoyayame](http://ms.shillest.net/yayame.xhtml) and either extract the NAR file as a ZIP or install the ghost so you can access its files
5. Refer to the [system dictionary](../system/yaya-shiori3-dic.md) and copy the files under the `system` folder
6. Copy `system_config.txt`
7. In `yaya.txt`, delete `dic,aya_shiori3.dic` and write `include, system_config.txt` instead
8. Open `config.dic` and set `SHIORI3FW.AUTO_DATA_CONVERT` to 1 and `SHIORI3FW.REF_ACCEL` to 0

These steps resolve most migration-related errors.

## For network distribution

For network distribution, `aya5.dll` and `aya5.txt` are no longer needed, so it is a good idea to delete them using a `delete.txt` file with the following contents, for example.

```
ghost/master/aya5.dll
ghost/master/aya5.txt
```

## Related

- [Creating a ghost with YAYA](./creating-ghost.md)
- [System dictionary/yaya_shiori3.dic](../system/yaya-shiori3-dic.md)
