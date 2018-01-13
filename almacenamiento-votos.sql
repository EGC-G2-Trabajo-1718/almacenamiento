
USE `almacenamiento`;

DROP TABLE IF EXISTS `votos`;
CREATE TABLE `votos` (
  `id` int(11) NOT NULL,
  `token_usuario` char(64) NOT NULL,
  `token_votacion` char(64) NOT NULL,
  `token_pregunta` char(64) NOT NULL,
  `token_respuesta` char(64) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=latin1;

ALTER TABLE `votos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `token_usuario, token_votacion, token_pregunta` (`token_usuario`,`token_votacion`,`token_pregunta`) USING BTREE;

ALTER TABLE `votos` CHANGE `id` `id` int(11) AUTO_INCREMENT;

ALTER TABLE `votos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=33;

DROP TABLE IF EXISTS `tokens`;
CREATE TABLE `tokens` (
  `id` int(11) NOT NULL,
  `token` char(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=latin1;

INSERT INTO `tokens` (`id`, `token`) VALUES
(1, 'QWERTY12345'),
(2, '12345QWERTY'),
(3, 'ASDFGH67890');

ALTER TABLE `tokens`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE (`token`);

ALTER TABLE `tokens` CHANGE `id` `id` int(11) AUTO_INCREMENT;

ALTER TABLE `tokens`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=33;