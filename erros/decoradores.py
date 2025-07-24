def gerenciar_conexao(func):
  def wrapper(self, *args, **kwards):
    try:
      if self._db.conectar():
        return func(self, *args, **kwards)
    finally:
      self._db.fechar()
  return wrapper