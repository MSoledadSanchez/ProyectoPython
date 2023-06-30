-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 30-06-2023 a las 17:05:20
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sportar`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `articulo`
--

CREATE TABLE `articulo` (
  `id` int(11) NOT NULL,
  `titulo` varchar(100) DEFAULT NULL,
  `descripcion` varchar(100) DEFAULT NULL,
  `category` varchar(20) DEFAULT NULL,
  `subcategory` varchar(20) DEFAULT NULL,
  `precio` int(11) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `image` varchar(400) DEFAULT NULL,
  `cuotas` int(11) DEFAULT NULL,
  `descuento` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `articulo`
--

INSERT INTO `articulo` (`id`, `titulo`, `descripcion`, `category`, `subcategory`, `precio`, `cantidad`, `image`, `cuotas`, `descuento`) VALUES
(1, 'Remera New Balance', 'Dry Fit Color Verde', 'Indumentaria', 'Remeras', 3500, 7, '../img/remera1.jpg', 3, 30),
(2, 'Remera Assys', 'Dry Fit Degrade Negro', 'Indumentaria', 'Remeras', 3500, 5, '../img/remera2.jpg', 0, 0),
(3, 'Remera DC', 'Escote en V Violeta', 'Indumentaria', 'Remeras', 3500, 10, '../img/remera1.jpg', 3, 30),
(4, 'Remera Under Armour', 'Driy Fit Azul Francia', 'Indumentaria', 'Remeras', 3500, 2, '../img/remera2.jpg', 0, 10),
(5, 'Zapatilla New Balance', 'Urban Gris', 'Calzado', 'Zapatillas', 10500, 8, '../img/remera1.jpg', 6, 0),
(6, 'Zapatilla Puma', 'Urban Blanca', 'Calzado', 'Zapatillas', 9000, 5, '../img/remera2.jpg', 0, 0),
(7, 'Pelota Qatar 2022', 'La pelota de los campeones', 'Accesorios', 'Pelotas', 6000, 20, '../img/remera1.jpg', 0, 0),
(8, 'Bolso Nike', 'Mediano Rosa y Negro', 'Accesorios', 'Bolso', 6200, 15, '../img/remera2.jpg', 0, 10),
(9, 'Campera Adidas', 'Basica Negra', 'Indumentaria', 'Camperas', 11500, 2, '../img/remera1.jpg', 3, 0),
(10, 'Campera Assys', 'Mujer Rosa Oscuro', 'Indumentaria', 'Camperas', 7800, 10, '../img/remera2.jpg', 0, 10);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `articulo`
--
ALTER TABLE `articulo`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `articulo`
--
ALTER TABLE `articulo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
