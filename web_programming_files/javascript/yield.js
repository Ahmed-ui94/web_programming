function range(from, to) {
    for(let i = from; i <= to; i++) {
        yield i;
    }
}
range(10, 20)