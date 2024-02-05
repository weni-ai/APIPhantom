import json

from django_ace import AceWidget as BaseAceWidget


class AceWidget(BaseAceWidget):
    def render(self, name, value, attrs=None, renderer=None):
        if self.mode == "json":
            try:
                value = json.dumps(json.loads(value), indent=4, sort_keys=True)
            except:
                pass
        return super().render(name, value, attrs, renderer)


def get_ace_widget(mode="python"):
    return AceWidget(
        mode=mode,
        theme="twilight",
        toolbar=True,
        width="100%",
        height="300px",
        fontsize="15px",
    )
