from dataclasses import dataclass
from typing import Any


class StateMachineException(Exception):
    ...


@dataclass
class State:
    name: str
    state_properties: dict[str, Any]


@dataclass
class Transition:
    source_name: str
    target_name: str

    def __str__(self) -> str:
        return f"Transition(from: {self.source_name}, to {self.target_name})"


class StateMachine:

    def __init__(self, states: tuple[State], transitions: tuple[Transition], start_node: str) -> None:
        self.states = {}

        for state in states:
            self.states[state.name] = {
                "state": state,
                "transitions": []
            }

        for transition in transitions:
            if self.states[transition.source_name]:
                self.states[transition.source_name]["transitions"].append(
                    transition.target_name)
            else:
                raise StateMachineException(
                    f"Unknown source in transition {transition}")

        self.start_node = start_node
        self.current_state = start_node

    def reset(self) -> None:
        self.current_state = self.start_node

    def travel(self, to: str) -> bool:
        available_transitions = self.states[self.current_state]["transitions"]

        if to in available_transitions:
            self.current_state = to
            print(self.current_state)
            return True
        print(self.current_state)
        return False

    def get_property(self, property: str) -> Any:
        state: State = self.states[self.current_state]["state"]
        return state.state_properties[property]
