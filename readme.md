## BlueAlliancePy

BlueAlliancePy is a Python-based client for Blue Alliance. It uses their JSON API to pull down info on teams and generate an HTML-formatted document on that info.

### Things to Keep in Mind
* This is truly a work-in-progress and will be super buggy and may not work at times.
* Bear with the single, one, lone developer \(me, lol\) when things get broken, and please wait for it to be fixed.
* This app uses *my* API key, so don't abuse it please.

### Libraries Used
* `time`
* `webbrowser`
* `requests`
* `json`
* `os`
* `random` (only used by the Kiosk)
* `sleep` from `time` (only used by the kiosk)

### Operating the Normal Client
Operating the normal client is easy. Run `Main.py`, follow the instructions, and boom.

### Operating the Kiosk
Operating the kiosk is a bit jank as of now. To operate the kiosk, run `Kiosk.py` and then follow the instructions. Then, when the browser opens, refresh the page until something appears. It will then auto-refresh from there. Sometimes it may come up with a blank page and not auto-refresh, this will be fixed soon.