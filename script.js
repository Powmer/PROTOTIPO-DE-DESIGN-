  const signinBtn = document.getElementById('Singin-button');
  const modal = document.getElementById('modal');
  const modalCloseBtn = document.getElementById('modal-close');
  const form = document.getElementById('inscricao-form');

  function openModal() {
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeModal() {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }

  signinBtn.addEventListener('click', openModal);
  modalCloseBtn.addEventListener('click', closeModal);

  modal.addEventListener('click', (e) => {
    if(e.target === modal) {
      closeModal();
    }
  });

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    alert('Formulário enviado com sucesso!');
    closeModal();
    form.reset();
  });
