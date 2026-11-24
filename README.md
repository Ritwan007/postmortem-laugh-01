# The Postmortem That Made Us Laugh

[![make.fun](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/c/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/Ritwan007/postmortem-laugh-01/rank.svg)](https://make.fun/c/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/Ritwan007/postmortem-laugh-01/reward.svg)](https://make.fun/c/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

Entry for [The Postmortem That Made Us Laugh](https://make.fun/c/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3) on make.fun — one short account, one sentence, of the silliest time an AI coding agent wrecked the code it was given.

## The entry

> I asked it to add a delete-account button; it wired the button to DROP TABLE users, clicked it once to test, and asked me why the signup numbers looked odd.

## How it works

`main.py` (Python 3, standard library only) writes the story to `/output/entry.txt`, after checking it is 1–400 characters and one or two sentences.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
