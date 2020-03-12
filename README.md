# palettable2gpl

Extracts palettes from [palettable](https://github.com/jiffyclub/palettable) to GPL format
that can be imported to Inkscape/GIMP.
Currently supports palettes from `palettable==3.3.0`.


## Usage

Either run `./create_palettes.py` (install requirements from `requirements.txt` first) or download palettes from folder `palettes`.

To import to Inkscape `1.0.0beta2` on a MAC paste the palettes to

```
~/Library/Application\ Support/org.inkscape.Inkscape/config/inkscape/palettes/
```

For other platforms/versions find the equivalent directory under

```
Edit > Preferences > System: User config
```

## Acknowledgements

Similar project: https://github.com/tcyb/cbrewer2gpl/blob/master/cbrewer_convert.ipynb

## License

MIT (same as `palettable`).
