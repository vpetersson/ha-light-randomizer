# Home Assistant Light Randomizer

This is a Home Assistant implementation of the old-school power plugs timers intended to turn on/off lights at random times when traveling to create the illusion of someone being home.

Since Home Assistant can already turn on/off lights, I thought it would be fun to re-create this but with a bit more intelligence.

## Installation

* Install and configure [pyscript](https://github.com/custom-components/pyscript)
* Copy in the scropt to the `pyscript` folder
* Create an automation as per below to trigger the script (modify it to fit your needs)


```yaml
- id: '1685281587370'
  alias: Random Lights.
  description: ''
  trigger:
  - platform: time_pattern
    hours: '*'
    minutes: '5'
  condition:
  - condition: state
    entity_id: input_boolean.home_toggle
    state: 'off'
  action:
  - service: pyscript.random_lights
    data: {}
  mode: single
```
