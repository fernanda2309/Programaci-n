# Estructura de <contacto>

# se importa modulo datetime
import datetime
# <contacto> se crea
class contacto:
  def _init_(self, nickname, nombre, correo, telefono, fechanacimiento,gasto):
    #nickname : nombre deseado po el contacto 
    #nombre: nombre del contacto
    #correo: correo electronico del contacto
    #telefono: numero telefonico del contacto
    #fechanacimiento: fecha nacimiento del contacto
    #gasto: Gasto mensual del contacto
    self.nickname = nickname
    self.nombre = nombre
    self.correo = correo
    self.telefono = telefono
    self.fechanacimiento = fechanacimiento
    self.gasto = gasto
