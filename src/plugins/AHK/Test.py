from src.plugins.AHK.NovaScript.NovaScript import NovaScript

register_script = NovaScript()

parameters = [
    "window_x",
    "window_y",
    "window_width",
    "window_height",
    "title"
]

values = [
    "100",
    "200",
    "300",
    "400",
    "Register Script"
]

it = dict()

for i in range(5):
    key = parameters[i]
    value = values[i]
    it[key] = value

register_script.setMetadata(it)

register_script.writeAHK("1")

register_script.read("RegisterTemplate.nova")