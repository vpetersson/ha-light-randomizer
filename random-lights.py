import random
import datetime

light_group = group.ikea_lights

@service
def random_lights():
    log.info(f'Started random light sequence.')
    turn_off_all_lights(light_group)
    select_random_lights_and_turn_on(light_group)

def turn_off_all_lights(light_group):
    log.info(f'Turning off all lights in {light_group.friendly_name}')
    for entity_id in light_group.entity_id:
        log.debug(f'Turning off {entity_id}')
        light.turn_off(entity_id=entity_id)

def select_random_lights_and_turn_on(light_group):
    all_lights = light_group.entity_id

    # @TODO: Filter out all unavailable lights.
    available_lights = all_lights

    num_lights_to_turn_on = min(len(available_lights), 5)
    selected_lights = random.sample(available_lights, num_lights_to_turn_on)
    log.info(f'Selected {num_lights_to_turn_on} lights to turn on: {selected_lights}')

    for entity_id in selected_lights:
        log.info(f'Turning on {entity_id}')
        light.turn_on(entity_id=entity_id)
