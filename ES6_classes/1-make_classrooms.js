import ClassRoom from "./0-classroom";
function initializeRooms() {
    return [
        ClassRoom(19),
        ClassRoom(20),
        ClassRoom(34)
    ];
}

const result = initializeRooms();
console.log(result);
