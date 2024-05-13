**This is a small proof of concept for dynamically creating Discord bot 
slash commands at runtime\* in Python.**

This allows users to create simple response slash commands using nothing
but the Discord app. There should be no programming experience necessary
for the end user. This is intended as a potential future feature to be
used in [FICSIT-Fred](https://github.com/Feyko/FICSIT-Fred). It would 
replace the existing usage of the message-content-based equivalent feature.

This requires the following to be implemented in the final product
- Usage of Fred's database instead of JSON, obviously
- Hot reload
    - *Is this part possible?
    - If not, would it be acceptable to just cold reload periodically?
- Permission checking so not just any schmuck can add commands
- Validation on the command name, because commands that don't match the 
pattern Discord prescribes (only 1-32 lowercase regex `\w` characters)