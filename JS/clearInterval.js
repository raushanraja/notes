function f() {
    const interval = setInterval(() => {
        const result = fetchData();
        console.log(result);
        if (result) {
            clearInterval(interval);
        }
    }, 1000);
}

function fetchData() {
    const randomInt = Math.floor(Math.random() * 100);
    if (randomInt % 2 == 0) {
        return false;
    }
    return false;
}

f();
