CREATE TABLE Departamentos (
  DepaID INT PRIMARY KEY,
  Nombre VARCHAR
);

CREATE TABLE Empleados (
  EmpleadoDPI INT PRIMARY KEY,
  Nombres VARCHAR,
  Apellidos VARCHAR,
  Sueldo DECIMAL,
  departamento_id INT,
  FOREIGN KEY (departamento_id) REFERENCES Departamentos(DepaID)
);

CREATE TABLE Usuario (
  EmpleadoDPI INT,
  Usuario VARCHAR,
  FOREIGN KEY (EmpleadoDPI) REFERENCES Empleados(EmpleadoDPI)
);

CREATE TABLE Carro (
  CarroID INT PRIMARY KEY,
  Marca VARCHAR,
  Modelo VARCHAR,
  Transmision VARCHAR
);

CREATE TABLE Repuestos (
  RepuestoID INT PRIMARY KEY,
  CarroID INT,
  Nombre VARCHAR,
  Categoria VARCHAR,
  Precio_Unitario DECIMAL,
  FOREIGN KEY (CarroID) REFERENCES Carro(CarroID)
);

CREATE TABLE Inventario (
  CarroID INT,
  RepuestoID INT,
  Existencia INT,
  Cantidad_Minima INT,
  FOREIGN KEY (CarroID) REFERENCES Carro(CarroID),
  FOREIGN KEY (RepuestoID) REFERENCES Repuestos(RepuestoID)
);

CREATE TABLE Cliente (
  NIT INT PRIMARY KEY,
  Nombre_Cliente VARCHAR,
  Contacto VARCHAR,
  Tipo VARCHAR
);

CREATE TABLE Venta (
  Numero_Orden INT PRIMARY KEY,
  CajaDPI INT,
  BodegaDPI INT,
  NIT INT,
  Total DECIMAL,
  MetodoPago VARCHAR,
  Fecha TIMESTAMP,
  FOREIGN KEY (NIT) REFERENCES Cliente(NIT)
);

CREATE TABLE Detalles_Venta (
  Numero_Orden INT,
  RepuestoID INT,
  Cantidad INT,
  Rebaja DECIMAL,
  SubTotal DECIMAL,
  FOREIGN KEY (Numero_Orden) REFERENCES Venta(Numero_Orden),
  FOREIGN KEY (RepuestoID) REFERENCES Repuestos(RepuestoID)
);

CREATE TABLE Comisiones (
  ComisionID INT PRIMARY KEY,
  EmpleadoDPI INT,
  NumOrden INT,
  Tipo VARCHAR,
  FOREIGN KEY (EmpleadoDPI) REFERENCES Empleados(EmpleadoDPI),
  FOREIGN KEY (NumOrden) REFERENCES Venta(Numero_Orden)
);

CREATE TABLE Pagos (
  MetodoPagoID INT PRIMARY KEY,
  MetodoPago VARCHAR,
  Usuario VARCHAR,
  EmpleadoDPI INT,
  FOREIGN KEY (EmpleadoDPI) REFERENCES Empleados(EmpleadoDPI)
);

CREATE TABLE Cotizacion (
  CotizacionID INT PRIMARY KEY,
  VendedorID INT,
  Total DECIMAL,
  Fecha TIMESTAMP,
  FOREIGN KEY (VendedorID) REFERENCES Empleados(EmpleadoDPI)
);

CREATE TABLE Cotizacion_Detalle (
  CotizacionDetalleID INT PRIMARY KEY,
  CotizacionID INT,
  RepuestoID INT,
  Cantidad INT,
  Precio_Unitario DECIMAL,
  Precio_Total DECIMAL,
  Numero_Linea INT,
  FOREIGN KEY (CotizacionID) REFERENCES Cotizacion(CotizacionID),
  FOREIGN KEY (RepuestoID) REFERENCES Repuestos(RepuestoID)
);

CREATE TABLE Compra_Carro (
  Fecha TIMESTAMP,
  Cantidad INT,
  CarroID INT,
  FOREIGN KEY (CarroID) REFERENCES Carro(CarroID)
);

CREATE TABLE Compra_Repuesto (
  CompraRepuestoID INT PRIMARY KEY,
  RepuestoID INT,
  Costo DECIMAL,
  ProveedorID INT,
  FOREIGN KEY (RepuestoID) REFERENCES Repuestos(RepuestoID),
  FOREIGN KEY (ProveedorID) REFERENCES Proveedor(ProveedorID)
);

CREATE TABLE Proveedor (
  ProveedorID INT PRIMARY KEY,
  Nombre VARCHAR,
  Direccion VARCHAR,
  Contacto VARCHAR
);

CREATE TABLE Bitacora_Alertas (
  AlertaID INT PRIMARY KEY,
  RepuestoID INT,
  Fecha TIMESTAMP,
  FOREIGN KEY (RepuestoID) REFERENCES Repuestos(RepuestoID)
);

CREATE TABLE Historial_Cambio (
  CambioID INT PRIMARY KEY,
  Tipo_Cambio VARCHAR,
  Tabla_Afectada VARCHAR,
  ID_Registro INT,
  Usuario VARCHAR,
  Fecha TIMESTAMP,
  Comentario VARCHAR
);

CREATE TABLE Cambios_Departamentos (
  Cambio_DepID INT PRIMARY KEY,
  EmpleadoDPI INT,
  Dep_Anterior VARCHAR,
  Dep_Nuevo VARCHAR,
  Fecha_Cambio TIMESTAMP,
  Motivo VARCHAR,
  FOREIGN KEY (EmpleadoDPI) REFERENCES Empleados(EmpleadoDPI)
);

CREATE TABLE Cambios_Salarios (
  Cambio_SalarioID INT PRIMARY KEY,
  EmpleadoDPI INT,
  Fecha_Cambio TIMESTAMP,
  Salario_Anterior DECIMAL,
  Salario_Nuevo DECIMAL,
  Motivo VARCHAR,
  FOREIGN KEY (EmpleadoDPI) REFERENCES Empleados(EmpleadoDPI)
);
