// plugins/axios.js
import axios from 'axios';

const instanciaAxios = axios.create({
    baseURL: 'https://backend-l8ve.onrender.com',  // URL base del backend de Flask
});

// Funciones para proyectos
export const createProject = (data, username, password) => {
    return instanciaAxios.post('/projects', data, {
        auth: {
            username: username,
            password: password
        }
    });
};
export const getProjects = () => instanciaAxios.get('/projects');
export const updateProject = (id, data) => instanciaAxios.put(`/projects/${id}`, data);
export const deleteProject = (id) => instanciaAxios.delete(`/projects/${id}`);

// Funciones para experiencias
export const createExperience = (data, username, password) => {
    return instanciaAxios.post('/experiences', data, {
        auth: {
            username: username,
            password: password
        }
    });
};
export const getExperiences = () => instanciaAxios.get('/experiences');
export const updateExperience = (id, data) => instanciaAxios.put(`/experiences/${id}`, data);
export const deleteExperience = (id) => instanciaAxios.delete(`/experiences/${id}`);

export default instanciaAxios;
