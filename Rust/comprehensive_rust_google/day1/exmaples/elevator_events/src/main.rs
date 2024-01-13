type Floor = i32;

#[derive(Debug)]
enum Button {
    LobbyCall(Direction, Floor),
    CarFloor(Floor),
}

#[derive(Debug)]
enum Event {
    ButtonPressed(Button),
    CarArrived(Floor),
    CarDoorOpened,
    CarDoorClosed,
}

#[derive(Debug)]
enum Direction {
    Up,
    Down,
}

fn process_event(event: Event) {
    match event {
        Event::ButtonPressed(button) => match button {
            Button::LobbyCall(dir, floor) => {
                println!("Lobby call button pressed: {:?} {:?}", dir, floor)
            }

            Button::CarFloor(floor) => {
                println!("Car floor button pressed: {:?}", floor)
            }
        },
        Event::CarArrived(floor) => {
            println!("Car arrived at floor: {:?}", floor)
        }
        Event::CarDoorOpened => {
            println!("Car door opened")
        }
        Event::CarDoorClosed => {
            println!("Car door closed")
        }
    }
}

fn car_arrived(floor: i32) -> Event {
    Event::CarArrived(floor)
}

fn car_door_opened() -> Event {
    Event::CarDoorOpened
}

fn car_door_closed() -> Event {
    Event::CarDoorClosed
}

fn lobby_call_button_pressed(floor: i32, dir: Direction) -> Event {
    Event::ButtonPressed(Button::LobbyCall(dir, floor))
}

fn car_floor_button_pressed(floor: i32) -> Event {
    Event::ButtonPressed(Button::CarFloor(floor))
}

fn main() {
    println!(
        "A ground floor passenger has pressed the up button: {:?}",
        lobby_call_button_pressed(0, Direction::Up)
    );
    println!(
        "The car has arrived on the ground floor: {:?}",
        car_arrived(0)
    );
    println!("The car door opened: {:?}", car_door_opened());
    println!(
        "A passenger has pressed the 3rd floor button: {:?}",
        car_floor_button_pressed(3)
    );
    println!("The car door closed: {:?}", car_door_closed());
    println!("The car has arrived on the 3rd floor: {:?}", car_arrived(3));
    process_event(car_arrived(3));
    process_event(lobby_call_button_pressed(3, Direction::Down));
}
