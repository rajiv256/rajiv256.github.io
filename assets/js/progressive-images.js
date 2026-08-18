(() => {
  const reveal = (image) => {
    const finish = () => {
      window.requestAnimationFrame(() => image.classList.add('is-loaded'));
    };

    if (typeof image.decode === 'function') {
      image.decode().then(finish).catch(finish);
    } else {
      finish();
    }
  };

  document.querySelectorAll('.post-body img').forEach((image) => {
    image.loading = 'lazy';
    image.decoding = 'async';

    if (image.complete) {
      reveal(image);
      return;
    }

    image.addEventListener('load', () => reveal(image), { once: true });
    image.addEventListener('error', () => image.classList.add('is-loaded'), { once: true });
  });
})();
