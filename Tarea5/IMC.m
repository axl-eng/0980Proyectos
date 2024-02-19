% Definiciòn de las categorias
InsP = "Insuficiencia Ponderal";
IntNorm = "Intervalo Normal";
SobreP = "Sobre Peso";
Obe1 = "Obesidad de Clase 1";
Obe2 = "Obesidad de Clase 2";
Obe3 = "Obesidad de Clase 3";

% Inicializar Variables

a = 0;
Usuarios = struct('Nombre', {}, 'Peso', {}, 'Altura', {}, 'IMC', {}, 'Categoria', {});

% Bucle Principal

while a==0 
fprintf ('\n--- Calculo IMC ---\n');
fprintf ('1. Calcular IMC\n');
fprintf ('2. Mostrar Datos\n');
fprintf ('3. Guardar Nuevos Datos En Archivo\n');
fprintf ('4. Leer Datos En Archivo\n');
fprintf ('5. Borrar Datos\n');
fprintf ('6. Salir\n');

Var = input ('Seleccione una opciòn: ');
switch Var
	case 1
	% Calcular IMC
	Nombre = input ('Ingrese el nombre del usuario: ', 's');
	Peso = input ('Ingrese el peso (kg): ');
	Altura = input ('Ingrese la altura (m): ');
	
	IMC = Peso/(Altura^2);
	
	% Categorizar IMC
	if IMC < 18.5
		Categoria = InsP;
	elseif IMC < 24.9
		Categoria = IntNorm;
	elseif IMC < 29.9
		Categoria = SobreP;
	elseif IMC < 34.9
		Categoria = Obe1;
	elseif IMC < 39.9
		Categoria = Obe2;
	else  
		Categoria = Obe3;
	end
	
	 % Mostrar resultados
            fprintf('IMC calculado: %.2f\n', IMC);
            fprintf('Categoría: %s\n', Categoria);

            % Almacenar datos en la estructura
            Usuarios(end+1).Nombre = Nombre;
            Usuarios(end).Peso = Peso;
            Usuarios(end).Altura = Altura;
            Usuarios(end).IMC = IMC;
            Usuarios(end).Categoria = Categoria;

        case 2
            % Mostrar datos de usuarios
            if isempty(Usuarios)
                fprintf('No hay datos para mostrar.\n');
            else
                for i = 1:length(Usuarios)
                    fprintf('\nUsuario %d:\n', i);
                    fprintf('Nombre: %s\n', Usuarios(i).Nombre);
                    fprintf('Peso: %.2f kg\n', Usuarios(i).Peso);
                    fprintf('Altura: %.2f m\n', Usuarios(i).Altura);
                    fprintf('IMC: %.2f\n', Usuarios(i).IMC);
                    fprintf('Categoría: %s\n', Usuarios(i).Categoria);
                end
            end

        case 3
            % Guardar datos en archivo
            if isempty(Usuarios)
                fprintf('No hay datos para guardar.\n');
            else
                datosimc = 'imc.txt';
                fid = fopen(datosimc, 'w');
                if fid == -1
                    fprintf('Error al abrir el archivo para escritura.\n');
                else
                    for i = 1:length(Usuarios)
                        fprintf(fid, '%s %.2f %.2f %.2f %s\n', Usuarios(i).Nombre, Usuarios(i).Peso, Usuarios(i).Altura, Usuarios(i).IMC, Usuarios(i).Categoria);
                    end
                    fclose(fid);
                    fprintf('Datos guardados en %s.\n', datosimc);
                end
            end

        case 4
            % Leer datos desde archivo
            datosimc = 'imc.txt';
            fid = fopen(datosimc, 'r');
            if fid == -1
                fprintf('Error al abrir el archivo para lectura.\n');
            else
                Usuarios = [];
                while ~feof(fid)
                    datos = fscanf(fid, '%s %f %f %f %s', [1, Inf]);
                    if ~isempty(datos)
                        Usuario.Nombre = datos{1};
                        Usuario.Peso = datos(2);
                        Usuario.Altura = datos(3);
                        Usuario.IMC = datos(4);
                        Usuario.Categoria = datos{5};
                        Usuarios = [Usuarios, Usuario];
                    end
                end
                fclose(fid);
                fprintf('Datos leídos desde %s.\n', datosimc);
            end

        case 5
            % Borrar datos
            Usuarios = struct('nombre', {}, 'peso', {}, 'altura', {}, 'IMC', {}, 'categoria', {});
            fprintf('Datos borrados.\n');

        case 6
            % Salir
            fprintf('Saliendo del programa.\n');
            a = 1; % Cambiar el valor de 'a' para salir del bucle

        otherwise
            fprintf('Opción no válida. Por favor, seleccione una opción válida.\n');
    end
end

