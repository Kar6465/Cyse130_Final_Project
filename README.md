# Thrones of Ashfall

**Team Members:** [Add your team names here]

---

## How to Run

1. Make sure Python 3 is installed
2. Clone the repository
3. From the project root, run:
```
python main.py
```
No external libraries required.

---

## Core Game Features

- 3 branching story paths with meaningful choices
- 6 endings based on player decisions
- 5 locations and major events
- 5 NPCs with dialogue and interactions
- Inventory system with 5 collectible items
- 2 challenges (puzzle + combat)
- Save/load system with tamper detection
- Audit logging to audit_log.txt
- Input validation throughout — game never crashes on bad input

---

## Story Paths and Endings

### Path 1: The Loyalist
You choose to restore the kingdom by finding and protecting Lady Elira, the last surviving royal heir. You ally with Ser Kael in the Great Hall and escort Elira to safety — or betray her.

### Path 2: The Shadow Path
You seek power through secrets. You descend into the War Room, meet Varyn the Whisperer, and attempt to crack an ancient terminal. Success gives you control over the kingdom from the shadows. Failure destroys the keep.

### Path 3: The Savior
You ignore politics and help survivors escape through the lower tunnels. Mira the Healer guides you to the people who need saving. The Warden blocks your path — you must fight through or fall.

---

### Endings

| Ending | Description |
|--------|-------------|
| Crown Restored | You protect Elira and she is crowned Queen. Peace returns to Valtheris. |
| Betrayer's Rise | You betray Elira and defeat Ser Kael in combat. You take power — but no one will ever trust you. |
| Master of Shadows | You solve the war room puzzle and seize control of an ancient weapon. You rule from the shadows. |
| Keep Destroyed | You fail the terminal puzzle. The alarm triggers and the keep collapses around you. |
| Silent Hero | You defeat the Warden and lead the survivors to safety through the tunnels. You disappear before anyone can ask your name. |
| Final Sacrifice | You hold the line against the Warden so the survivors can escape. You do not make it out. |

---

## Locations / Events

1. **Prison Cell** — Opening scene. Player wakes up, finds the Rusty Key and a cryptic note, and escapes into the halls.
2. **Castle Halls** — The branching point. Player chooses their path: Loyalist, Shadow, or Savior.
3. **Great Hall** — Major event. Ser Kael tests your loyalty and gives you the Royal Sigil Ring.
4. **War Room** — Major event. Varyn the Whisperer hands over the Secret Map and Ancient Code Scroll. Player attempts to hack the terminal.
5. **Lower Tunnels** — Major event. Mira the Healer gives you Healing Herbs. The Warden blocks the escape route.
6. **Royal Chapel** — Major decision event. Player meets Lady Elira and chooses to protect or betray her.

---

## NPCs

| NPC | Location | Role |
|-----|----------|------|
| Ser Kael | Great Hall | Tests loyalty, gives Royal Sigil Ring, fights player if betrayed |
| Lady Elira | Royal Chapel | Central to Loyalist path — protect or betray her determines the ending |
| Varyn the Whisperer | War Room | Gives Secret Map and Ancient Code Scroll, unlocks the Shadow path |
| Mira the Healer | Lower Tunnels | Gives Healing Herbs, guides survivors, support character for Savior path |
| The Warden | Lower Tunnels | Boss enemy blocking the escape route — must be defeated in combat |

---

## Inventory Items

| Item | Where Found | Purpose |
|------|-------------|---------|
| Rusty Key | Prison Cell | Opens the cell and early doors |
| Royal Sigil Ring | Great Hall | Gains trust from loyalists, required for Loyalist path |
| Ancient Code Scroll | War Room | Contains the riddle hint for the terminal puzzle |
| Secret Map | War Room | Unlocks hidden paths through the keep |
| Healing Herbs | Lower Tunnels | Restores 30 HP during combat challenges |

---

## Challenges

### Challenge 1: War Room Puzzle (War Room)
**What the player must do:** Solve a riddle displayed on the ancient terminal and enter the correct authorization code. Players have 3 attempts.

**Success:** The terminal unlocks — leads to the Master of Shadows ending.

**Failure:** Security breach triggers a lockdown — leads to the Keep Destroyed ending.

---

### Challenge 2: Combat (Warden Fight / Ser Kael Fight)
**What the player must do:** Turn-based combat. Each round the player picks Attack (deal damage), Defend (take reduced damage), or Use Healing Herbs (restore HP). Combat ends when either combatant reaches 0 HP.

**Warden Fight:**
- Success → Silent Hero ending
- Failure → Final Sacrifice ending

**Ser Kael Fight (triggered by betraying Elira):**
- Success → Betrayer's Rise ending
- Failure → Crown Restored ending

---

## Cyber Pack

### 1. Input Validation + Safe Error Handling
All menus use `try/except` blocks to catch non-integer input. The game re-prompts the player instead of crashing. Invalid choices outside the valid range are also caught and re-prompted.

### 2. Audit Logging
All security-relevant events are written to `audit_log.txt` with a timestamp. Logged events include:
- Game start and end
- Challenge attempts (success and failure)
- Save and load attempts (success and failure, including tamper detection)

### 3. Save / Load with Tamper Detection
Game state is saved to `savegame.txt` in plain text. A SHA-256 hash of the save contents is stored separately in `savegame.txt.hash`. On load, the hash is recomputed and compared — if they don't match, the save is rejected as tampered and the player is notified.
