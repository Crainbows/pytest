echo "
feat: add hat wobble
├───┘-├─────────────┘
│         │
│         └─> Summary in present tense.
│
├─> chore: add Oyster build script
├─> docs: explain hat wobble
├─> feat: add beta sequence
├─> fix: remove broken confirmation message
├─> refactor: share logic between 4d3d3d3 and flarhgunnstow
├─> style: convert tabs to spaces
└─> test: ensure Tayne retains clothing
"

while true; do
	read -p "$* Have you used the above git message format? [y/n]: " yn
        case $yn in
            [Yy]*) exit 0  ;;  
	    [Nn]*) exit 1 ;;
	esac
done
