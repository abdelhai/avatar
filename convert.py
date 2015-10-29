import CloudConvert
import time




def svg_png(svg):
    temp_png = 'temp_{}.png'.format(str(time.time()).replace('.', '-'))
    apikey = "wC16nGlz4WpEEsG5z8PdCXKUbGT1HwDpSHNozNo1uNtiNGhmI034qyiV-zE2KgCNLSp1TNPitFF002Tz_vlqoQ"
    process = CloudConvert.ConversionProcess(apikey)

    # This should autodetect file extension. if not, you can
    # always set process.fromformat and .toformat to the correct
    # values
    process.init("template.svg", "output.png")

    # This step uploads the file and starts the conversion.
    # If you pass `wait=True` the request will block until the
    # conversion is finished.
    process.start()

    # Alternatively, this block until file is done processing.
    # process.wait_for_completion(check_interval=5)  # Interval in seconds

    # Returns a file-like obj to download the processed file
    download = process.download()

    with open(temp_png, "wb") as f:  # Important to set mode to wb
        f.write(download.read())
    return temp_png
