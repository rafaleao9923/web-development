function preloadImage(url) {
    return new Promise((resolve, reject) => {
        const img = new Image();
        img.onload = () => resolve(img);
        img.onerror = reject;
        img.src = url;
    });
}

async function preloadNextPageImages(cards) {
    const imagePromises = cards.flatMap(card => [
        preloadImage(card.header_img),
        preloadImage(card.profile_img)
    ]);
    await Promise.all(imagePromises);
}

async function loadNextPage() {
    if (isLoading || reachedEnd) return;
    
    isLoading = true;
    const cards = await getData(currentPage);
    
    if (cards.length === 0) {
        reachedEnd = true;
        isLoading = false;
        return;
    }

    await preloadNextPageImages(cards);

    cards.forEach((card, index) => {
        const globalIndex = (currentPage - 1) * 6 + index;
        loadCard(card, globalIndex + 1, index);
    });

    currentPage++;
    setTimeout(() => {
        isLoading = false;
    }, 500 * cards.length);
}