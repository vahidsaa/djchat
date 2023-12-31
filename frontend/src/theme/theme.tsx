import { createTheme, responsiveFontSizes } from '@mui/material/styles';

declare module '@mui/material/styles'{
    interface Theme{
        primaryAppBar: {
            height : number;
        };
        primaryDraw: {
            width : number;
            closed: number;
        };
        SecondaryDraw: {
            width : number;
        };
    }
    interface ThemeOptions {
        primaryAppBar: {
            height:number;
        };
        primaryDraw: {
            width : number;
            closed: number;
        };
        SecondaryDraw: {
            width : number;
        };
    }
}


export const createMuiTheme = () => {
    let theme = createTheme({

        
        typography: {
            fontFamily: ['IBM Plex Serif', "sans-serif",].join(","),
        },
        primaryAppBar: {
            height: 50,
        },
        primaryDraw:{
            width:240,
            closed: 70,
        },
        SecondaryDraw: {
            width : 240,
        },
        components:{
            MuiAppBar: {
                defaultProps:{
                    color: "default",
                    elevation: 0,
                }
            }
        }
    });
    theme = responsiveFontSizes(theme);
    return theme;
};

export default createMuiTheme;