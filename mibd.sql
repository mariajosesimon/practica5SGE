-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 03-04-2021 a las 19:38:43
-- Versión del servidor: 10.4.18-MariaDB
-- Versión de PHP: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `mibd`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `idCliente` int(11) NOT NULL,
  `Nombre` varchar(255) NOT NULL,
  `Apellidos` varchar(255) NOT NULL,
  `Ciudad` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `NIF` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamentos`
--

CREATE TABLE `departamentos` (
  `idDepartamento` int(11) NOT NULL,
  `NombreDepartamento` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `facturascompras`
--

CREATE TABLE `facturascompras` (
  `idFacturaCompra` int(11) NOT NULL,
  `idPresupuestoCompra` int(11) NOT NULL,
  `FechaCompra` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `facturasventas`
--

CREATE TABLE `facturasventas` (
  `idFacturaVenta` int(11) NOT NULL,
  `idPresupuestoVenta` int(11) NOT NULL,
  `FechaCompra` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ordenproduccion`
--

CREATE TABLE `ordenproduccion` (
  `idOrden` int(11) NOT NULL,
  `idProductoFinal` int(11) NOT NULL,
  `FechaOrden` date NOT NULL,
  `idProductor` int(11) NOT NULL,
  `cantidadProducida` int(11) NOT NULL,
  `idProducto` int(11) NOT NULL,
  `Cantidad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `presupuestoscompras`
--

CREATE TABLE `presupuestoscompras` (
  `idPresupuesto` int(11) NOT NULL,
  `idProveedor` int(11) NOT NULL,
  `FechaPresupuesto` date NOT NULL,
  `idComprador` int(11) NOT NULL,
  `idProducto` int(11) NOT NULL,
  `Cantidad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `presupuestosventas`
--

CREATE TABLE `presupuestosventas` (
  `idPresupuesto` int(11) NOT NULL,
  `idCliente` int(11) NOT NULL,
  `FechaPresupuesto` date NOT NULL,
  `idVendedor` int(11) NOT NULL,
  `idProducto` int(11) NOT NULL,
  `Cantidad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productoscomprados`
--

CREATE TABLE `productoscomprados` (
  `idProducto` int(11) NOT NULL,
  `NombreProducto` varchar(100) NOT NULL,
  `Precio` double NOT NULL,
  `Stock` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productoscreados`
--

CREATE TABLE `productoscreados` (
  `idProducto` int(11) NOT NULL,
  `NombreProducto` varchar(100) NOT NULL,
  `Precio` double NOT NULL,
  `Stock` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedores`
--

CREATE TABLE `proveedores` (
  `idProveedor` int(11) NOT NULL,
  `Nombre` varchar(255) NOT NULL,
  `Apellidos` varchar(255) NOT NULL,
  `Ciudad` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `CIF` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `idUsuario` int(11) NOT NULL,
  `NombreUSR` varchar(50) NOT NULL,
  `ApellidosUSR` varchar(100) NOT NULL,
  `NIF` varchar(10) NOT NULL,
  `FechaAlta` date NOT NULL,
  `FechaBaja` date DEFAULT NULL,
  `Activo` int(1) NOT NULL,
  `idDepartamento` int(11) NOT NULL,
  `usuario` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL,
  `email` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`idCliente`);

--
-- Indices de la tabla `departamentos`
--
ALTER TABLE `departamentos`
  ADD PRIMARY KEY (`idDepartamento`);

--
-- Indices de la tabla `facturascompras`
--
ALTER TABLE `facturascompras`
  ADD PRIMARY KEY (`idFacturaCompra`),
  ADD KEY `FK_pCo_id` (`idPresupuestoCompra`);

--
-- Indices de la tabla `facturasventas`
--
ALTER TABLE `facturasventas`
  ADD PRIMARY KEY (`idFacturaVenta`),
  ADD KEY `FK_pVe_id` (`idPresupuestoVenta`);

--
-- Indices de la tabla `ordenproduccion`
--
ALTER TABLE `ordenproduccion`
  ADD PRIMARY KEY (`idOrden`),
  ADD KEY `FK_idProd` (`idProducto`),
  ADD KEY `FK_usu_id` (`idProductor`),
  ADD KEY `FK_pfi_id` (`idProductoFinal`);

--
-- Indices de la tabla `presupuestoscompras`
--
ALTER TABLE `presupuestoscompras`
  ADD PRIMARY KEY (`idPresupuesto`) USING BTREE,
  ADD KEY `FK_prod_id` (`idProducto`),
  ADD KEY `FK_prov_id` (`idProveedor`),
  ADD KEY `FK_user_id` (`idComprador`);

--
-- Indices de la tabla `presupuestosventas`
--
ALTER TABLE `presupuestosventas`
  ADD PRIMARY KEY (`idPresupuesto`) USING BTREE,
  ADD KEY `FK_cli_id` (`idCliente`),
  ADD KEY `FK_usr_id` (`idVendedor`),
  ADD KEY `FK_pro_id` (`idProducto`);

--
-- Indices de la tabla `productoscomprados`
--
ALTER TABLE `productoscomprados`
  ADD PRIMARY KEY (`idProducto`);

--
-- Indices de la tabla `productoscreados`
--
ALTER TABLE `productoscreados`
  ADD PRIMARY KEY (`idProducto`);

--
-- Indices de la tabla `proveedores`
--
ALTER TABLE `proveedores`
  ADD PRIMARY KEY (`idProveedor`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`idUsuario`),
  ADD UNIQUE KEY `usuario` (`usuario`),
  ADD KEY `FK_dep_id` (`idDepartamento`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `idCliente` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `departamentos`
--
ALTER TABLE `departamentos`
  MODIFY `idDepartamento` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `facturascompras`
--
ALTER TABLE `facturascompras`
  MODIFY `idFacturaCompra` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `facturasventas`
--
ALTER TABLE `facturasventas`
  MODIFY `idFacturaVenta` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `ordenproduccion`
--
ALTER TABLE `ordenproduccion`
  MODIFY `idOrden` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `productoscomprados`
--
ALTER TABLE `productoscomprados`
  MODIFY `idProducto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `productoscreados`
--
ALTER TABLE `productoscreados`
  MODIFY `idProducto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `proveedores`
--
ALTER TABLE `proveedores`
  MODIFY `idProveedor` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `idUsuario` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `facturascompras`
--
ALTER TABLE `facturascompras`
  ADD CONSTRAINT `FK_pCo_id` FOREIGN KEY (`idPresupuestoCompra`) REFERENCES `presupuestoscompras` (`idPresupuesto`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `facturasventas`
--
ALTER TABLE `facturasventas`
  ADD CONSTRAINT `FK_pVe_id` FOREIGN KEY (`idPresupuestoVenta`) REFERENCES `presupuestosventas` (`idPresupuesto`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `ordenproduccion`
--
ALTER TABLE `ordenproduccion`
  ADD CONSTRAINT `FK_idProd` FOREIGN KEY (`idProducto`) REFERENCES `productoscomprados` (`idProducto`) ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_pfi_id` FOREIGN KEY (`idProductoFinal`) REFERENCES `productoscreados` (`idProducto`) ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_usu_id` FOREIGN KEY (`idProductor`) REFERENCES `usuarios` (`idUsuario`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `presupuestoscompras`
--
ALTER TABLE `presupuestoscompras`
  ADD CONSTRAINT `FK_prod_id` FOREIGN KEY (`idProducto`) REFERENCES `productoscomprados` (`idProducto`) ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_prov_id` FOREIGN KEY (`idProveedor`) REFERENCES `proveedores` (`idProveedor`) ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_user_id` FOREIGN KEY (`idComprador`) REFERENCES `usuarios` (`idUsuario`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `presupuestosventas`
--
ALTER TABLE `presupuestosventas`
  ADD CONSTRAINT `FK_cli_id` FOREIGN KEY (`idCliente`) REFERENCES `clientes` (`idCliente`) ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_pro_id` FOREIGN KEY (`idProducto`) REFERENCES `productoscomprados` (`idProducto`) ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_usr_id` FOREIGN KEY (`idVendedor`) REFERENCES `usuarios` (`idUsuario`) ON UPDATE CASCADE,
  ADD CONSTRAINT `presupuestosventas_ibfk_1` FOREIGN KEY (`idCliente`) REFERENCES `clientes` (`idCliente`) ON DELETE NO ACTION ON UPDATE CASCADE;

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `FK_dep_id` FOREIGN KEY (`idDepartamento`) REFERENCES `departamentos` (`idDepartamento`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
