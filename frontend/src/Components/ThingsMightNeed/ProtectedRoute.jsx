import {useAuth} from './Auth'
import { Navigate } from "react-router-dom";


const ProtectedRoute = ({ children }) => {
    const { user } = useAuth();

    if (!user) {
        return <Navigate to="/Header" />;
    }

    return children;
};

//export default ProtectedRoute;