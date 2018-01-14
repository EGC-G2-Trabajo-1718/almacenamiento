
USE `almacenamiento`;

DROP TABLE IF EXISTS `votos`;
CREATE TABLE `votos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `token_usuario` char(64) NOT NULL,
  `token_votacion` char(64) NOT NULL,
  `token_pregunta` char(64) NOT NULL,
  `token_respuesta` char(64) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token_usuario, token_votacion, token_pregunta` (`token_usuario`,`token_votacion`,`token_pregunta`) USING BTREE
);

DROP TABLE IF EXISTS `tokens`;
CREATE TABLE `tokens` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `token` char(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE (`token`)
);

INSERT INTO `tokens` (`id`, `token`) VALUES
(1, 'QWERTY12345'),
(2, '12345QWERTY'),
(3, 'ASDFGH67890');