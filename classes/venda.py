from classes.produto import Produto

class Venda(Produto):

  def __init__(self, idVenda:int, data, idProduto:int, quantidade:int, valorTotal: float):
    self.idVenda = idVenda
    self.data = data
    self.idProduto = idProduto
    self.quantidade = quantidade
    self.valorTotal = valorTotal
  
  def registrarVenda(self):
    pass