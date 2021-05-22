# phpMyAdmin SQL Dump
# version 5.1.0
# https://www.phpmyadmin.net/
#
# Servidor: 127.0.0.1
# Tiempo de generación: 20-05-2021 a las 20:33:11
# Versión del servidor: 10.4.18-MariaDB
# Versión de PHP: 8.0.3

#SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
#START TRANSACTION;
#SET time_zone = "+00:00";



#
# Base de datos: `mibd2`
#

# ############################

#
# Estructura de tabla para la tabla `clientes`
#
clientes="CREATE TABLE IF NOT EXISTS `clientes` (   `idCliente` int(11) NOT NULL,   `Nombre` varchar(255) NOT NULL,   `Apellidos` varchar(255) NOT NULL,   `Ciudad` varchar(50) NOT NULL,   `Telefono` int(11) DEFAULT NULL,   `NIF` varchar(10) NOT NULL,   `Email` varchar(50) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"


# ############################

#
# Estructura de tabla para la tabla `departamentos`
#
 departamentos="CREATE TABLE IF NOT EXISTS `departamentos` (   `idDepartamento` int(11) NOT NULL,   `NombreDepartamento` varchar(25) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
#
# Volcado de datos para la tabla `departamentos`
#
 insertdepartamentos="INSERT INTO `departamentos` (`idDepartamento`, `NombreDepartamento`) VALUES (1, 'RRHH'), (2, 'Compras'), (3, 'Ventas'), (4, 'Produccion');"

# ############################

#
# Estructura de tabla para la tabla `facturacomprasproductos`
#
 facturacomprasproductos="CREATE TABLE IF NOT EXISTS `facturacomprasproductos` (   `idFactura` int(11) NOT NULL,   `idProducto` int(11) NOT NULL,   `Cantidad` int(11) NOT NULL,   `idConcepto` int(11) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;" 
# ############################

#
# Estructura de tabla para la tabla `facturascompras`
#
 facturascompras="CREATE TABLE IF NOT EXISTS `facturascompras` (   `idFactura` int(11) NOT NULL,   `nFactura` int(11) NOT NULL,   `idProveedor` int(11) NOT NULL,   `FechaFactura` date NOT NULL,   `idComprador` int(11) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"

# ############################

#
# Estructura de tabla para la tabla `facturasventas`
#
 facturasventas="CREATE TABLE IF NOT EXISTS `facturasventas` (   `idFactura` int(11) NOT NULL,   `nFactura` int(11) NOT NULL,   `idCliente` int(11) NOT NULL,   `FechaFactura` date NOT NULL,   `idVendedor` int(11) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;" 
# ############################

#
# Estructura de tabla para la tabla `facturaventasproductos`
#
 facturaventasproductos="CREATE TABLE IF NOT EXISTS `facturaventasproductos` (   `idFactura` int(11) NOT NULL,   `idProducto` int(11) NOT NULL,   `Cantidad` int(11) NOT NULL,   `idConcepto` int(11) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"  # ############################

#
# Estructura de tabla para la tabla `ordenproduccion`
#
 ordenproduccion="CREATE TABLE IF NOT EXISTS `ordenproduccion` (   `idOrden` int(11) NOT NULL,   `idProductoFinal` int(11) NOT NULL,   `FechaOrden` date NOT NULL,   `idProductor` int(11) NOT NULL,   `cantidadProducida` int(11) DEFAULT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;" 
# ############################

#
# Estructura de tabla para la tabla `presupuestoscompras`
#
 presupuestoscompras="REATE TABLE IF NOT EXISTS `presupuestoscompras` (   `idPresupuesto` int(11) NOT NULL,   `idProveedor` int(11) NOT NULL,   `FechaPresupuesto` date NOT NULL,   `idComprador` int(11) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"

# ############################

#
# Estructura de tabla para la tabla `presupuestoscomprasproductos`
#
 presupuestoscomprasproductos="CREATE TABLE IF NOT EXISTS `presupuestoscomprasproductos` (   `idPresupuesto` int(11) NOT NULL,   `idProducto` int(11) NOT NULL,   `Cantidad` int(11) NOT NULL,   `idConcepto` int(11) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;" 
# ############################

#
# Estructura de tabla para la tabla `presupuestosventas`
#
 presupuestosventas="CREATE TABLE IF NOT EXISTS `presupuestosventas` (   `idPresupuesto` int(11) NOT NULL,   `idCliente` int(11) NOT NULL,   `FechaPresupuesto` date NOT NULL,   `idVendedor` int(11) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"

# ############################

#
# Estructura de tabla para la tabla `presupuestosventasproductos`
#
 presupuestosventasproductos="CREATE TABLE IF NOT EXISTS `presupuestosventasproductos` (   `idPresupuesto` int(11) NOT NULL,   `idProducto` int(11) NOT NULL,   `Cantidad` int(11) NOT NULL,   `idPVP` int(11) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;" 
# ############################

#
# Estructura de tabla para la tabla `productoscomprados`
#

productoscomprados="CREATE TABLE IF NOT EXISTS `productoscomprados` (   `idProducto` int(11) NOT NULL,   `NombreProducto` varchar(100) NOT NULL,   `Precio` double NOT NULL,   `Stock` int(11) NOT NULL DEFAULT 0 ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"

# ############################

#
# Estructura de tabla para la tabla `productoscreados`
#

productoscreados="CREATE TABLE IF NOT EXISTS `productoscreados` (   `idProducto` int(11) NOT NULL,   `NombreProducto` varchar(100) NOT NULL,   `Precio` double NOT NULL,   `Stock` int(11) DEFAULT 0 ) ENGINE=InnoDB DEFAULT CHARSET=utf8;" 
# ############################

#
# Estructura de tabla para la tabla `productosutilizadosproduccion`
#

productosutilizadosproduccion="CREATE TABLE IF NOT EXISTS `productosutilizadosproduccion` (   `idProductosUtilizadosOrden` int(11) NOT NULL,   `idOrden` int(11) NOT NULL,   `idProductoUtilizado` int(11) NOT NULL,   `Cantidad` int(11) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

# ############################

#
# Estructura de tabla para la tabla `proveedores`
#

proveedores="CREATE TABLE IF NOT EXISTS `proveedores` (   `idProveedor` int(11) NOT NULL,   `Nombre` varchar(255) NOT NULL,   `Ciudad` varchar(50) NOT NULL,   `Telefono` int(11) NOT NULL,   `CIF` varchar(10) NOT NULL,   `Email` varchar(50) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

# ############################

#
# Estructura de tabla para la tabla `userlogin`
#

userlogin="CREATE TABLE IF NOT EXISTS `userlogin` (   `idUsuario` int(11) NOT NULL DEFAULT 0,   `NombreUSR` varchar(50) NOT NULL,   `ApellidosUSR` varchar(100) NOT NULL,   `NIF` varchar(10) NOT NULL,   `FechaAlta` date NOT NULL,   `FechaBaja` date DEFAULT NULL,   `Activo` int(1) NOT NULL,   `idDepartamento` int(11) NOT NULL,   `usuario` varchar(25) NOT NULL,   `password` varchar(25) NOT NULL,   `email` varchar(50) DEFAULT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

# ############################

#
# Estructura de tabla para la tabla `usuarios`
#

usuarios="CREATE TABLE IF NOT EXISTS `usuarios` (   `idUsuario` int(11) NOT NULL,   `NombreUSR` varchar(50) NOT NULL,   `ApellidosUSR` varchar(100) NOT NULL,   `NIF` varchar(10) NOT NULL,   `FechaAlta` date NOT NULL,   `FechaBaja` date DEFAULT NULL,   `Activo` int(1) NOT NULL,   `idDepartamento` int(11) NOT NULL,   `usuario` varchar(25) NOT NULL,   `password` varchar(25) NOT NULL,   `email` varchar(50) DEFAULT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

#
# Índices para tablas volcadas
#

#
# Indices de la tabla `clientes`
#
clientesMod="ALTER TABLE `clientes`   ADD PRIMARY KEY (`idCliente`);"

#
# Indices de la tabla `departamentos`
#
departamentosIND="ALTER TABLE `departamentos`   ADD PRIMARY KEY (`idDepartamento`);"

#
# Indices de la tabla `facturacomprasproductos`
#
facturacomprasproductosIND="ALTER TABLE `facturacomprasproductos`   ADD PRIMARY KEY (`idConcepto`),   ADD KEY `FK_idf_fac` (`idFactura`),   ADD KEY `FK_idp_pro` (`idProducto`); "
#
# Indices de la tabla `facturascompras`
#
facturascomprasIND="ALTER TABLE `facturascompras`   ADD PRIMARY KEY (`idFactura`),   ADD KEY `FK_fco_id` (`idComprador`),   ADD KEY `FK_fco_pro` (`idProveedor`);"

#
# Indices de la tabla `facturasventas`
#
facturasventasIND="ALTER TABLE `facturasventas`   ADD PRIMARY KEY (`idFactura`),   ADD KEY `FK_fve_id` (`idVendedor`),   ADD KEY `FK_fve_pro` (`idCliente`);"

#
# Indices de la tabla `facturaventasproductos`
#
facturaventasproductosIND="ALTER TABLE `facturaventasproductos`   ADD PRIMARY KEY (`idConcepto`),   ADD KEY `FK_idv_fac` (`idFactura`),   ADD KEY `FK_idv_pro` (`idProducto`);"

#
# Indices de la tabla `ordenproduccion`
#
ordenproduccionIND="ALTER TABLE `ordenproduccion`   ADD PRIMARY KEY (`idOrden`),   ADD KEY `FK_opr_id` (`idProductor`),   ADD KEY `FK_pfi_idp` (`idProductoFinal`);"

#
# Indices de la tabla `presupuestoscompras`
#
presupuestoscomprasIND="ALTER TABLE `presupuestoscompras`   ADD PRIMARY KEY (`idPresupuesto`) USING BTREE,   ADD KEY `FK_pco_idU` (`idComprador`),   ADD KEY `FK_pco_pro` (`idProveedor`);"

#
# Indices de la tabla `presupuestoscomprasproductos`
#
presupuestoscomprasproductosIND="ALTER TABLE `presupuestoscomprasproductos`   ADD PRIMARY KEY (`idConcepto`),   ADD KEY `FK_idp_pre` (`idPresupuesto`),   ADD KEY `FK_idp_prd` (`idProducto`);"

#
# Indices de la tabla `presupuestosventas`
#
presupuestosventasIND="ALTER TABLE `presupuestosventas`   ADD PRIMARY KEY (`idPresupuesto`),   ADD KEY `FK_pve_idU` (`idVendedor`),   ADD KEY `FK_pve_pro` (`idCliente`);"

#
# Indices de la tabla `presupuestosventasproductos`
#
presupuestosventasproductosIND="ALTER TABLE `presupuestosventasproductos`   ADD PRIMARY KEY (`idPVP`),   ADD KEY `FK_pvp_prd` (`idProducto`),   ADD KEY `FK_pvp_pre` (`idPresupuesto`);"

#
# Indices de la tabla `productoscomprados`
#
productoscompradosIND="ALTER TABLE `productoscomprados`   ADD PRIMARY KEY (`idProducto`);"

#
# Indices de la tabla `productoscreados`
#
productoscreadosIND="ALTER TABLE `productoscreados`   ADD PRIMARY KEY (`idProducto`);"

#
# Indices de la tabla `productosutilizadosproduccion`
#
productosutilizadosproduccionIND="ALTER TABLE `productosutilizadosproduccion`   ADD PRIMARY KEY (`idProductosUtilizadosOrden`),   ADD KEY `FK_pup_idO` (`idOrden`),   ADD KEY `FK_pup_iPU` (`idProductoUtilizado`);"

#
# Indices de la tabla `proveedores`
#
proveedoresMOD1="ALTER TABLE `proveedores`   ADD PRIMARY KEY (`idProveedor`);"

#
# Indices de la tabla `usuarios`
#
usuariosMOD="ALTER TABLE `usuarios`   ADD PRIMARY KEY (`idUsuario`),   ADD KEY `FK_dep_id` (`idDepartamento`);"

#
# AUTO_INCREMENT de las tablas volcadas
#

#
# AUTO_INCREMENT de la tabla `clientes`
#
clientesMOD="ALTER TABLE `clientes`   MODIFY `idCliente` int(11) NOT NULL AUTO_INCREMENT;"

#
# AUTO_INCREMENT de la tabla `departamentos`
#
departamentosMOD="ALTER TABLE `departamentos`   MODIFY `idDepartamento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;"

#
# AUTO_INCREMENT de la tabla `facturacomprasproductos`
#
facturacomprasproductosMOD="ALTER TABLE `facturacomprasproductos`   MODIFY `idConcepto` int(11) NOT NULL AUTO_INCREMENT;"

#
# AUTO_INCREMENT de la tabla `facturascompras`
#
facturascomprasMOD="ALTER TABLE `facturascompras`   MODIFY `idFactura` int(11) NOT NULL AUTO_INCREMENT;"

#
# AUTO_INCREMENT de la tabla `facturasventas`
#
facturasventasMOD="ALTER TABLE `facturasventas`   MODIFY `idFactura` int(11) NOT NULL AUTO_INCREMENT;"

#
# AUTO_INCREMENT de la tabla `facturaventasproductos`
#
facturaventasproductosMOD="ALTER TABLE `facturaventasproductos`   MODIFY `idConcepto` int(11) NOT NULL AUTO_INCREMENT;"

#
# AUTO_INCREMENT de la tabla `ordenproduccion`
#
ordenproduccionMOD="ALTER TABLE `ordenproduccion`   MODIFY `idOrden` int(11) NOT NULL AUTO_INCREMENT;"

#
# AUTO_INCREMENT de la tabla `presupuestoscompras`
#
presupuestoscomprasMOD="ALTER TABLE `presupuestoscompras`   MODIFY `idPresupuesto` int(11) NOT NULL AUTO_INCREMENT;"

#
# AUTO_INCREMENT de la tabla `presupuestoscomprasproductos`
#
presupuestoscomprasproductosMOD="ALTER TABLE `presupuestoscomprasproductos`   MODIFY `idConcepto` int(11) NOT NULL AUTO_INCREMENT;"

#
# AUTO_INCREMENT de la tabla `presupuestosventas`
#
presupuestosventasMOD="ALTER TABLE `presupuestosventas`   MODIFY `idPresupuesto` int(11) NOT NULL AUTO_INCREMENT;"

#
# AUTO_INCREMENT de la tabla `presupuestosventasproductos`
#
presupuestosventasproductosMOD="ALTER TABLE `presupuestosventasproductos`   MODIFY `idPVP` int(11) NOT NULL AUTO_INCREMENT;"

#
# AUTO_INCREMENT de la tabla `productoscomprados`
#
productoscompradosMOD="ALTER TABLE `productoscomprados`   MODIFY `idProducto` int(11) NOT NULL AUTO_INCREMENT;"

#
# AUTO_INCREMENT de la tabla `productoscreados`
#
productoscreadosMOD="ALTER TABLE `productoscreados`   MODIFY `idProducto` int(11) NOT NULL AUTO_INCREMENT;"

#
# AUTO_INCREMENT de la tabla `productosutilizadosproduccion`
#
productosutilizadosproduccionMOD="ALTER TABLE `productosutilizadosproduccion`   MODIFY `idProductosUtilizadosOrden` int(11) NOT NULL AUTO_INCREMENT;"

#
# AUTO_INCREMENT de la tabla `proveedores`
#
proveedoresMOD="ALTER TABLE `proveedores`   MODIFY `idProveedor` int(11) NOT NULL AUTO_INCREMENT;"

#
# AUTO_INCREMENT de la tabla `usuarios`
#
usuariosMOD1="ALTER TABLE `usuarios`   MODIFY `idUsuario` int(11) NOT NULL AUTO_INCREMENT;"

#
# Restricciones para tablas volcadas
#

#
# Filtros para la tabla `facturacomprasproductos`
#
facturacomprasproductosMOD="ALTER TABLE `facturacomprasproductos`   ADD CONSTRAINT `FK_idf_fac` FOREIGN KEY (`idFactura`) REFERENCES `facturascompras` (`idFactura`) ON DELETE CASCADE ON UPDATE CASCADE,   ADD CONSTRAINT `FK_idp_pro` FOREIGN KEY (`idProducto`) REFERENCES `productoscomprados` (`idProducto`) ON DELETE CASCADE ON UPDATE CASCADE; "
#
# Filtros para la tabla `facturascompras`
#
facturascomprasMOD="ALTER TABLE `facturascompras`   ADD CONSTRAINT `FK_fco_id` FOREIGN KEY (`idComprador`) REFERENCES `usuarios` (`idUsuario`) ON DELETE CASCADE ON UPDATE CASCADE,   ADD CONSTRAINT `FK_fco_pro` FOREIGN KEY (`idProveedor`) REFERENCES `proveedores` (`idProveedor`) ON DELETE CASCADE ON UPDATE CASCADE; "
#
# Filtros para la tabla `facturasventas`
#
facturasventasMOD="ALTER TABLE `facturasventas`   ADD CONSTRAINT `FK_fve_id` FOREIGN KEY (`idVendedor`) REFERENCES `usuarios` (`idUsuario`) ON DELETE CASCADE ON UPDATE CASCADE,   ADD CONSTRAINT `FK_fve_pro` FOREIGN KEY (`idCliente`) REFERENCES `clientes` (`idCliente`) ON DELETE CASCADE ON UPDATE CASCADE; "
#
# Filtros para la tabla `facturaventasproductos`
#
facturaventasproductosMOD="ALTER TABLE `facturaventasproductos`   ADD CONSTRAINT `FK_idv_fac` FOREIGN KEY (`idFactura`) REFERENCES `facturasventas` (`idFactura`) ON DELETE CASCADE ON UPDATE CASCADE,   ADD CONSTRAINT `FK_idv_pro` FOREIGN KEY (`idProducto`) REFERENCES `productoscreados` (`idProducto`) ON DELETE CASCADE ON UPDATE CASCADE,   ADD CONSTRAINT `facturaventasproductos_ibfk_1` FOREIGN KEY (`idFactura`) REFERENCES `facturasventas` (`idFactura`) ON DELETE CASCADE ON UPDATE CASCADE,   ADD CONSTRAINT `facturaventasproductos_ibfk_2` FOREIGN KEY (`idProducto`) REFERENCES `productoscreados` (`idProducto`) ON DELETE CASCADE ON UPDATE CASCADE; "
#
# Filtros para la tabla `ordenproduccion`
#
ordenproduccionMOD="ALTER TABLE `ordenproduccion`   ADD CONSTRAINT `FK_opr_id` FOREIGN KEY (`idProductor`) REFERENCES `usuarios` (`idUsuario`) ON DELETE CASCADE ON UPDATE CASCADE,   ADD CONSTRAINT `FK_pfi_idp` FOREIGN KEY (`idProductoFinal`) REFERENCES `productoscreados` (`idProducto`) ON DELETE CASCADE ON UPDATE CASCADE; "
#
# Filtros para la tabla `presupuestoscompras`
#
presupuestoscomprasMOD="ALTER TABLE `presupuestoscompras`   ADD CONSTRAINT `FK_pco_idU` FOREIGN KEY (`idComprador`) REFERENCES `usuarios` (`idUsuario`) ON DELETE CASCADE ON UPDATE CASCADE,   ADD CONSTRAINT `FK_pco_pro` FOREIGN KEY (`idProveedor`) REFERENCES `proveedores` (`idProveedor`) ON DELETE CASCADE ON UPDATE CASCADE; "
#
# Filtros para la tabla `presupuestoscomprasproductos`
#
presupuestoscomprasproductosMOD="ALTER TABLE `presupuestoscomprasproductos`   ADD CONSTRAINT `FK_idp_prd` FOREIGN KEY (`idProducto`) REFERENCES `productoscomprados` (`idProducto`) ON DELETE CASCADE ON UPDATE CASCADE,   ADD CONSTRAINT `FK_idp_pre` FOREIGN KEY (`idPresupuesto`) REFERENCES `presupuestoscompras` (`idPresupuesto`) ON DELETE CASCADE ON UPDATE CASCADE; "
#
# Filtros para la tabla `presupuestosventas`
#
presupuestosventasMOD="ALTER TABLE `presupuestosventas`   ADD CONSTRAINT `FK_pve_idU` FOREIGN KEY (`idVendedor`) REFERENCES `usuarios` (`idUsuario`) ON DELETE CASCADE ON UPDATE CASCADE,   ADD CONSTRAINT `FK_pve_pro` FOREIGN KEY (`idCliente`) REFERENCES `clientes` (`idCliente`) ON DELETE CASCADE ON UPDATE CASCADE; "
#
# Filtros para la tabla `presupuestosventasproductos`
#
presupuestosventasproductosMOD="ALTER TABLE `presupuestosventasproductos`   ADD CONSTRAINT `FK_pvp_prd` FOREIGN KEY (`idProducto`) REFERENCES `productoscreados` (`idProducto`) ON DELETE CASCADE ON UPDATE CASCADE,   ADD CONSTRAINT `FK_pvp_pre` FOREIGN KEY (`idPresupuesto`) REFERENCES `presupuestosventas` (`idPresupuesto`) ON DELETE CASCADE ON UPDATE CASCADE; "
#
# Filtros para la tabla `productosutilizadosproduccion`
#
productosutilizadosproduccionMOD="ALTER TABLE `productosutilizadosproduccion`   ADD CONSTRAINT `FK_pup_iPU` FOREIGN KEY (`idProductoUtilizado`) REFERENCES `productoscomprados` (`idProducto`) ON DELETE CASCADE ON UPDATE CASCADE,   ADD CONSTRAINT `FK_pup_idO` FOREIGN KEY (`idOrden`) REFERENCES `ordenproduccion` (`idOrden`) ON DELETE CASCADE ON UPDATE CASCADE; "
#
# Filtros para la tabla `usuarios`
#
usuariosMOD="ALTER TABLE `usuarios`   ADD CONSTRAINT `FK_dep_id` FOREIGN KEY (`idDepartamento`) REFERENCES `departamentos` (`idDepartamento`) ON DELETE CASCADE ON UPDATE CASCADE; COMMIT;"


